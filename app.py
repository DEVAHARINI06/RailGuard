"""
RailGuard Streamlit Application
Run: streamlit run app.py
"""

import os
import json
import sqlite3
from datetime import datetime
from collections import Counter

import numpy as np
import streamlit as st
from PIL import Image

st.set_page_config(page_title="RailGuard", page_icon="🚆", layout="wide")

MODELS_DIR = "models"
CNN_PATH = os.path.join(MODELS_DIR, "best_cnn_model.keras")
AE_PATH = os.path.join(MODELS_DIR, "autoencoder.keras")
AE_THRESHOLD_PATH = os.path.join(MODELS_DIR, "ae_threshold.json")
YOLO_PATH = os.path.join(MODELS_DIR, "best.pt")

DB_PATH = "railguard_history.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS inspections(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        filename TEXT,
        recommendation TEXT
    )
    """)
    conn.commit()
    conn.close()


@st.cache_resource
def load_models():
    from tensorflow.keras.models import load_model
    from ultralytics import YOLO

    cnn_model = load_model(CNN_PATH)
    ae_model = load_model(AE_PATH)
    yolo_model = YOLO(YOLO_PATH)

    with open(AE_THRESHOLD_PATH) as f:
        threshold = json.load(f)["threshold"]

    return cnn_model, ae_model, yolo_model, threshold


def analyze_image(path, cnn_model, ae_model, yolo_model, threshold):
    from tensorflow.keras.preprocessing import image as keras_image

    result = {}

    # YOLO
    yolo_results = yolo_model(path, conf=0.10, verbose=False)

    detections = []
    for box in yolo_results[0].boxes:
        detections.append({
            "class": yolo_model.names[int(box.cls)],
            "confidence": float(box.conf)
        })

    result["yolo_detections"] = detections

    result["filtered_detections"] = [
        d for d in detections
        if d["class"].lower() != "no defect"
    ]

    os.makedirs("annotated_temp", exist_ok=True)
    annotated_path = os.path.join(
        "annotated_temp",
        os.path.basename(path)
    )
    yolo_results[0].save(filename=annotated_path)
    result["annotated_path"] = annotated_path

    # CNN
    img = keras_image.load_img(path, target_size=(224, 224))
    arr = keras_image.img_to_array(img) / 255.0
    arr = np.expand_dims(arr, axis=0)

    pred = cnn_model.predict(arr, verbose=0)[0][0]

    result["cnn_classification"] = (
        "Non defective" if pred > 0.5 else "Defective"
    )
    result["cnn_confidence"] = float(pred if pred > 0.5 else 1 - pred)

    # Autoencoder
    ae_img = keras_image.load_img(path, target_size=(128, 128))
    ae_arr = keras_image.img_to_array(ae_img) / 255.0
    ae_arr = np.expand_dims(ae_arr, axis=0)

    recon = ae_model.predict(ae_arr, verbose=0)
    mse = np.mean(np.square(ae_arr - recon))

    result["is_anomaly"] = mse > threshold
    result["reconstruction_error"] = float(mse)

    # Recommendation
    if len(result["filtered_detections"]) > 0:
        result["recommendation"] = "Immediate Repair"
    elif result["is_anomaly"]:
        result["recommendation"] = "Manual Inspection"
    elif result["cnn_classification"] == "Defective" and result["cnn_confidence"] > 0.95:
        result["recommendation"] = "Schedule Maintenance"
    else:
        result["recommendation"] = "Continue Monitoring"

    return result


def summarize(detections):
    if not detections:
        return "No defects detected"

    counts = Counter([d["class"] for d in detections])
    return ", ".join(f"{v}x {k}" for k, v in counts.items())


def main():
    init_db()

    st.title("🚆 RailGuard")

    cnn_model, ae_model, yolo_model, threshold = load_models()

    file = st.file_uploader(
        "Upload railway image",
        type=["jpg", "jpeg", "png"]
    )

    if file:
        os.makedirs("temp_uploads", exist_ok=True)
        path = os.path.join("temp_uploads", file.name)

        with open(path, "wb") as f:
            f.write(file.getbuffer())

        result = analyze_image(
            path,
            cnn_model,
            ae_model,
            yolo_model,
            threshold
        )

        col1, col2 = st.columns(2)

        with col1:
            st.image(path, caption="Uploaded Image")

        with col2:
            st.image(
                result["annotated_path"],
                caption="YOLO Detection"
            )

        st.metric(
            "CNN Classification",
            result["cnn_classification"],
            f'{result["cnn_confidence"]*100:.1f}%'
        )

        st.metric(
            "Anomaly",
            "Yes" if result["is_anomaly"] else "No"
        )

        st.metric(
            "Defects Localized",
            len(result["filtered_detections"])
        )

        st.write(summarize(result["filtered_detections"]))
        st.success(result["recommendation"])


if __name__ == "__main__":
    main()
