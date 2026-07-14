# Literature Survey — Railway Track Defect Detection (RailGuard)

## Paper 1
**Title:** Rail Surface Defect Detection Method Based on YOLOv3 Deep Learning Networks
**Authors / Venue:** S. Yanan, Z. Hui, L. Li, Z. Hang — 2018 Chinese Automation Congress (CAC), IEEE
**Year:** 2018
**Problem Statement:** Manual and traditional machine-vision inspection of rail surface defects lacks comprehensiveness, speed, and accuracy.
**Proposed Solution:** Resizes rail images to 416×416, applies YOLOv3 with dimensional-clustering bounding box prediction and binary cross-entropy loss for single-pass defect localization.
**Limitation:** Detects only bounding-box location, not defect shape or exact size; accuracy trade-off for speed noted in later comparative studies.

## Paper 2
**Title:** A Study on Railway Surface Defects Detection Based on Machine Vision (Improved YOLOv4 + MobileNetV3)
**Authors / Venue:** Entropy (MDPI) journal
**Year:** 2021
**Problem Statement:** Existing deep-learning detectors (e.g., YOLOv3/v4) have large model sizes, high parameter counts, and slow inference, limiting real-time deployment.
**Proposed Solution:** Replaces YOLOv4's backbone with lightweight MobileNetV3 and applies depthwise-separable convolution on the PANet neck, cutting parameters and model size while raising accuracy over baseline YOLOv4.
**Limitation:** Gains are tied to a specific field-collected dataset with added Gaussian noise; generalization to other rail imaging conditions not fully verified.

## Paper 3
**Title:** Deep Convolutional Neural Networks for Detection of Rail Surface Defects
**Authors / Venue:** S. Faghih-Roohi, S. Hajizadeh, A. Núñez, R. Babuska, B. De Schutter — IJCNN 2016, IEEE
**Year:** 2016
**Problem Statement:** Manual review of massive video-recording archives for rail surface defects is infeasible; hand-crafted feature extraction is difficult and unreliable.
**Proposed Solution:** Proposes and compares several CNN architectures of varying size/activation functions as automated feature learners for defect classification directly from rail images.
**Limitation:** Larger networks improve accuracy but need longer training time; purely classification-based, no defect localization.

## Paper 4
**Title:** An Unsupervised-Learning-Based Approach for Automated Defect Inspection on Textured Surfaces
**Authors / Venue:** S. Mei, H. Yang, Z. Yin — IEEE Transactions on Instrumentation and Measurement
**Year:** 2018
**Problem Statement:** Defective samples are rare relative to normal samples, making supervised defect classification data-imbalanced or infeasible on textured/industrial surfaces.
**Proposed Solution:** Trains a convolutional autoencoder exclusively on defect-free images; reconstruction error at multiple Gaussian pyramid scales is used to flag and localize anomalies.
**Limitation:** Threshold selection is empirical and dataset-dependent; performance drops on highly irregular or non-repetitive textures.

## Paper 5
**Title:** Automated Railway Track Defect Detection System using YOLO Deep Learning Algorithm
**Authors / Venue:** International Journal of Engineering Research & Technology (IJERT)
**Year:** 2025
**Problem Statement:** Sensor-based methods (accelerometers, GPR, eddy current) detect specific fault types only and need complex equipment; CNNs classify well but localize poorly, while two-stage detectors (R-CNN, Faster R-CNN) are too slow for real-time monitoring.
**Proposed Solution:** Reviews and adopts YOLO's single-stage, single-pass architecture as the balance point between classification accuracy and real-time detection speed for track defect monitoring.
**Limitation:** Comparative claims are drawn from surveyed literature rather than a unified head-to-head benchmark on one dataset.

---
*Compiled for RailGuard project report — Section 3, Literature Survey.*
