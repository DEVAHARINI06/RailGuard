# RailGuard Dashboard — Local Setup

## 1. Install Python

Python 3.9–3.11 recommended. Check with:
```
python --version
```

## 2. Set up a virtual environment (recommended)

```
python -m venv railguard-env
# Windows:
railguard-env\Scripts\activate
# Mac/Linux:
source railguard-env/bin/activate
```

## 3. Install dependencies

```
pip install -r requirements.txt
```

This may take a few minutes (TensorFlow and Ultralytics are large packages).

## 4. Download your trained models from Google Drive

From your Colab `RailGuard/models` folder, download these 4 files to your computer:

- `best_cnn_model.keras`
- `autoencoder.keras`
- `ae_threshold.json`
- `yolo_defect_v2/weights/best.pt` — **rename this one to `yolo_defect_v2_best.pt`** when you save it locally (the nested folder structure doesn't matter once renamed)

You can download files from Google Drive by right-clicking each one → Download.

## 5. Arrange your folder like this

```
railguard_app/
├── app.py
├── requirements.txt
├── README.md
└── models/
    ├── best_cnn_model.keras
    ├── autoencoder.keras
    ├── ae_threshold.json
    └── yolo_defect_v2_best.pt
```

Create the `models` folder yourself and drop the 4 downloaded files into it.

## 6. Run the dashboard

```
streamlit run app.py
```

This opens automatically in your browser at `http://localhost:8501`.

## 7. Using it

Upload a railway track image (jpg/png). The dashboard will show:
- The original image and YOLO's annotated detection
- CNN classification (Defective / Non defective) with confidence
- Autoencoder anomaly check
- A final maintenance recommendation (Continue Monitoring / Schedule Maintenance / Immediate Repair)

Inspection history is saved locally to `railguard_history.db` (SQLite) and shown in the sidebar.

## Troubleshooting

- **"Could not load models" error** — double-check the `models/` folder has all 4 files with the exact names listed above.
- **Slow first prediction** — TensorFlow and YOLO take a few seconds to warm up on first use; this is normal.
- **Port already in use** — run `streamlit run app.py --server.port 8502` instead.