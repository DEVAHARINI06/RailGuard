# Project Proposal

## RailGuard: Railway Safety and Predictive Maintenance System

---

## 1. Introduction

Railway tracks are conventionally inspected manually or at scheduled
intervals using visual walkthroughs, ultrasonic testing, or geometry
measurement vehicles. While effective to a degree, these methods are slow,
labor-intensive, and prone to inconsistency between inspectors. Undetected
defects — cracks, broken rails, corrosion, or loose fasteners — can escalate
into serious safety incidents if not caught early.

RailGuard proposes an automated, deep learning-based alternative: a system
that analyzes railway track images to detect defects, classify their
severity, flag unusual anomalies, and recommend a maintenance action —
reducing dependence on manual inspection while improving detection
consistency and speed.

## 2. Problem Statement

Manual and traditional sensor-based inspection methods face three core
limitations:

1. **Inconsistency** — detection quality depends on inspector experience and
   attentiveness.
2. **Limited frequency** — inspections happen on a schedule, not
   continuously, leaving gaps where defects can develop unnoticed.
3. **Cost** — specialized equipment (ultrasonic rigs, geometry cars) is
   expensive and cannot be deployed everywhere.

RailGuard addresses this by using computer vision and deep learning to
automate defect detection from ordinary track images, making inspection
faster, more consistent, and less dependent on specialized hardware.

## 3. Objectives

- Automatically detect railway track defects from images.
- Classify detected defects by severity / type (defective vs. non-defective).
- Detect unusual or previously unseen abnormalities using unsupervised
  learning.
- Recommend an appropriate maintenance action based on combined model
  outputs.
- Present results through an accessible dashboard for end users.

## 4. Proposed System

RailGuard combines three deep learning models, each targeting a different
aspect of the inspection problem:

| Model | Task | Technique |
|---|---|---|
| YOLOv8n | Defect localization | Object detection (transfer learning from COCO) |
| CNN (MobileNetV2) | Defective / Non-defective classification | Transfer learning, binary classification |
| Autoencoder | Anomaly detection | Unsupervised reconstruction-based learning |

Outputs from all three models are combined through a rule-based
recommendation layer that produces one of three verdicts: **Continue
Monitoring**, **Schedule Maintenance**, or **Immediate Repair**.

## 5. Scope

This project is developed as a **proof-of-concept** using publicly available
datasets (Kaggle's Railway Track Fault Detection dataset and a Roboflow
rail-defect object detection dataset), given the constraints of a student
project (no access to specialized inspection hardware, GPS-tagged sensor
data, or large proprietary defect archives). The system demonstrates the
architectural approach and pipeline design used in commercial railway
inspection systems, at a scale appropriate for academic evaluation.

## 6. Technologies Used

| Component | Technology |
|---|---|
| Programming Language | Python |
| Object Detection | YOLOv8 (Ultralytics) |
| Classification | CNN (MobileNetV2, TensorFlow/Keras) |
| Anomaly Detection | Convolutional Autoencoder (TensorFlow/Keras) |
| Image Processing | OpenCV, Pillow |
| Dashboard | Streamlit |
| Database | SQLite |
| Training Environment | Google Colab (GPU) |

## 7. Expected Outcomes

- A trained CNN classifier distinguishing defective from non-defective track
  images with a measurable, test-set-validated accuracy.
- A trained autoencoder capable of flagging anomalous track images based on
  a systematically tuned reconstruction-error threshold.
- A trained YOLOv8 model capable of localizing and classifying visible
  defects, evaluated honestly against the constraints of a small training
  dataset.
- An integrated pipeline combining all three models into a single
  maintenance recommendation.
- A working Streamlit dashboard for interactive use and demonstration.

## 8. Limitations and Honest Framing

Given the use of small, publicly available datasets rather than
proprietary, large-scale industrial data:

- The YOLOv8 detector's recall is limited by the small number of training
  images per class — it is presented as a proof-of-concept rather than a
  production-ready detector.
- The CNN and Autoencoder, trained on a moderately sized, cleaner dataset,
  achieve more reliable, presentable metrics.

This is addressed directly in the Evaluation section of the project report
rather than being hidden, in line with good engineering and academic
practice.
