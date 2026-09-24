# Construction Safety Computer Vision

Real-time computer vision for construction-site safety monitoring using PPE detection, pose estimation, ergonomic risk screening, and edge inference.

## Research Context

This repository is a personal portfolio implementation inspired by the author's work on construction safety computer vision and is related to the published paper:

**A Unified Edge-Based Framework for Construction Safety: Expert-Calibrated Spatial Fusion, REBA-Driven Ergonomics, and Automated Incident Response**

Published in *International Journal of Computational Intelligence Systems* (Springer), 2026.

DOI: https://doi.org/10.1007/s44196-026-01506-6

> **Note:** This repository is an independently written implementation for demonstration and portfolio purposes. It is not the official implementation of the published paper and does not reproduce collaborator code.

## Pipeline

Video / Camera → PPE / Object Detection → Worker Detection & Association → Pose Estimation → Joint-Angle / Ergonomic Features → Risk Screening & Visualization → Annotated Video + Metrics

## Features

- YOLO-based PPE/object detection
- Human pose estimation
- Worker-level detection and visualization
- Joint-angle calculation from pose landmarks
- Transparent REBA-inspired ergonomic screening
- Video and webcam inference
- FPS and latency benchmarking
- Configurable inference settings
- Edge-oriented deployment workflow

## Installation

pip install -r requirements.txt

Place compatible model weights in models/. Model weights and datasets are intentionally excluded from this repository.

## Run Inference

python scripts/run_inference.py --source path/to/video.mp4 --ppe-model models/ppe.pt --pose-model models/yolo11n-pose.pt

For webcam input:

python scripts/run_inference.py --source 0 --ppe-model models/ppe.pt --pose-model models/yolo11n-pose.pt

## Benchmark

python scripts/benchmark.py --source path/to/video.mp4 --pose-model models/yolo11n-pose.pt

Benchmark results depend on model weights, input resolution, hardware, and runtime configuration.

## Published Research Results

The associated publication reports **0.910 mAP@50** and approximately **14.2 FPS** on constrained edge hardware with 4 GB VRAM under the experimental configuration described in the paper. These figures are publication results and should not be interpreted as benchmarks reproduced by this repository unless independently verified.

## Limitations

- PPE detection quality depends on the selected dataset and trained weights.
- Pose estimation can degrade under occlusion, poor lighting, and unusual camera angles.
- The ergonomic component is a transparent screening implementation and is **not a complete official REBA assessment**.
- Real deployment requires site-specific validation, camera calibration, threshold tuning, and safety review.

## Roadmap

- Multi-camera worker tracking
- Configurable PPE class mappings
- Improved temporal risk aggregation
- Dashboard for incident analytics
- Edge deployment profiling
- Reproducible evaluation scripts

## Citation

If you reference the research behind this project, please cite:

> Luhadia, S. V., et al. “A Unified Edge-Based Framework for Construction Safety: Expert-Calibrated Spatial Fusion, REBA-Driven Ergonomics, and Automated Incident Response.” *International Journal of Computational Intelligence Systems*, 2026. https://doi.org/10.1007/s44196-026-01506-6

## Author

**Sarthak Vishal Luhadia**  
Computer Vision • AI/ML • AR/VR