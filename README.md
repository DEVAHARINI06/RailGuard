# RailGuard — Railway Safety and Predictive Maintenance System

Deep learning system combining YOLOv8 (defect detection), a CNN (defect
classification), and an Autoencoder (anomaly detection) to inspect railway
track images and recommend maintenance actions, presented through a
Streamlit dashboard.

## Project structure

```
RailGuard/
├── app.py                     <- Streamlit dashboard (run this)
├── requirements.txt           <- Python dependencies
├── README.md                  <- this file
├── models/                    <- PUT YOUR 4 DOWNLOADED MODEL FILES HERE
│   ├── PLACE_MODELS_HERE.txt  <- instructions, delete once models are added
│   ├── best_cnn_model.keras   <- (you add this)
│   ├── autoencoder.keras      <- (you add this)
│   ├── ae_threshold.json      <- (you add this)
│   └── yolo_defect_v2_best.pt <- (you add this, renamed from best.pt)
└── training_scripts/          <- reference copies of the Colab training code
    ├── train_cnn.py
    ├── train_autoencoder.py
    └── train_yolo.py
```

The `training_scripts/` folder is included so your project has a complete,
reproducible pipeline on record — but you do NOT need to run these locally.
They were already run in Google Colab, and their trained outputs are the
4 model files you need to download and place in `models/`.

## Setup (VS Code / local machine)

### 1. Get the 4 trained model files

These only exist in your Google Drive (Colab saved them there during
training) — they are NOT part of this download. Go to Google Drive →
`RailGuard/models/` and download:

- `best_cnn_model.keras`
- `autoencoder.keras`
- `ae_threshold.json`
- `yolo_defect_v2/weights/best.pt` → rename to `yolo_defect_v2_best.pt`

Place all 4 inside this project's `models/` folder.

### 2. Create a virtual environment

```
python -m venv venv
```
Windows:
```
venv\Scripts\activate
```
Mac/Linux:
```
source venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

This installs Streamlit, TensorFlow, Ultralytics (YOLO), Pillow, and NumPy.
It may take a few minutes — TensorFlow and Ultralytics are large.

### 4. Run the dashboard

```
streamlit run app.py
```

This opens automatically in your browser at `http://localhost:8501`.

## Using the dashboard

1. Upload a railway track image (jpg/png)
2. View side-by-side: original image + YOLO-annotated detection
3. See CNN classification (Defective / Non defective) with confidence
4. See Autoencoder anomaly status and reconstruction error
5. Get a final maintenance recommendation: Continue Monitoring / Schedule
   Maintenance / Immediate Repair
6. Inspection history is logged automatically to a local SQLite database
   (`railguard_history.db`) and shown in the sidebar

## Troubleshooting

- **"Could not load models" error** — check `models/` has all 4 files with
  the exact names listed above (case-sensitive).
- **Slow first prediction** — TensorFlow/YOLO take a few seconds to warm up
  on first use; this is normal.
- **Port already in use** — run `streamlit run app.py --server.port 8502`.
- **pip install fails / very slow** — make sure your virtual environment is
  activated (you should see `(venv)` in your terminal prompt) before running
  `pip install -r requirements.txt`.

## Model summary

| Model | Task | Result |
|---|---|---|
| CNN (MobileNetV2 transfer learning) | Defective / Non-defective classification | 81.82% test accuracy |
| Autoencoder | Anomaly detection on unseen defect types | Threshold tuned: 42% detection rate at 10% false-positive rate |
| YOLOv8n | Bounding-box defect localization | Proof-of-concept; limited by small (51-image) training set |
