# Construction Safety Computer Vision

Research code for a real-time construction-site safety monitoring system combining PPE detection, worker tracking, pose-based ergonomic analysis, incident logging, reporting, and automated alert routing.

## Research Context

This repository contains the application implementation used in the co-authored construction-safety research project:

**A Unified Edge-Based Framework for Construction Safety: Expert-Calibrated Spatial Fusion, REBA-Driven Ergonomics, and Automated Incident Response**

Published in *International Journal of Computational Intelligence Systems* (Springer), 2026.

DOI: https://doi.org/10.1007/s44196-026-01506-6

The core application code in `app.py` is reproduced from the public research implementation by **Daksh Singla**:

https://github.com/dakshSingla1904/Tri-State-Construction-Safety-CV

This repository is maintained as Sarthak Vishal Luhadia's research/project repository. The original implementation and its contributors should be credited when the code is reused.

## What the Application Implements

- YOLO-based construction PPE/object detection
- Multi-model inference modes
- Weighted Boxes Fusion for combining detections
- Worker bounding-box smoothing and tracking
- PPE-to-worker association
- Pose-based ergonomic analysis
- Fall detection
- Temporal violation tracking
- Safety/compliance scoring
- Incident snapshots and CSV audit logging
- Flask-based monitoring interface
- Video, image, and webcam processing
- Background video processing
- Normal and slow-motion exports
- Automated PDF safety reports
- Optional SMTP-based alert routing

## Repository Structure

```text
construction-safety-computer-vision/
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
├── README.md
├── .gitignore
└── pose_analysis.py        # standalone pose-analysis experiment
```

## Installation

Create a Python environment and install the dependencies:

```bash
pip install -r requirements.txt
```

The application expects the trained model weights used by the research implementation. These weights are **not included** in this repository.

The original application expects model files under:

```text
weights/
├── m1_medium.pt
├── m2_medium.pt
└── m_small.pt
```

and the YOLO pose model:

```text
yolo11n-pose.pt
```

Only use model weights and datasets that you are authorized to use or redistribute.

## Running the Application

From the repository root:

```bash
python app.py
```

The Flask application runs on port 5000 by default.

Open the local application in a browser after the server starts.

## Pose Analysis

A separate pose-analysis script is included as an experimental/standalone implementation. It uses YOLO11 pose tracking and calculates posture angles from keypoints.

The uploaded pose implementation calculates:

- trunk/back angle
- neck angle
- worker tracking IDs
- SAFE/BAD posture classification
- reasons for flagged posture

For example, the source calculates a back angle from the shoulder, hip, and knee midpoints and flags excessive bending when the angle falls below its configured threshold. fileciteturn44file0L69-L88

The same script also uses YOLO tracking with persistent IDs and the COCO pose keypoints used for shoulders, hips, and knees. fileciteturn44file0L37-L50

## Research Results

The associated publication reports **0.910 mAP@50** and approximately **14.2 FPS** on constrained edge hardware with 4 GB VRAM under the experimental setup described in the paper.

These are **published research results** and should not be presented as independently reproduced benchmarks unless the experiment is reproduced.

## Configuration and Security

The application contains optional SMTP/RPA alert functionality. Do **not** commit real Gmail passwords, app passwords, recipient credentials, or other secrets to GitHub.

Use environment variables or another secret-management mechanism before deploying the alert functionality outside a local research environment.

Generated uploads, exports, reports, incident images, model weights, and other runtime artifacts should remain outside version control.

## Citation

If you use the research or application, cite the published work:

> Luhadia, S. V., et al. “A Unified Edge-Based Framework for Construction Safety: Expert-Calibrated Spatial Fusion, REBA-Driven Ergonomics, and Automated Incident Response.” *International Journal of Computational Intelligence Systems*, 2026. https://doi.org/10.1007/s44196-026-01506-6

## Attribution

Core application implementation:
**Daksh Singla et al.**  
Public implementation: https://github.com/dakshSingla1904/Tri-State-Construction-Safety-CV

Repository maintainer:
**Sarthak Vishal Luhadia**

Computer Vision • AI/ML • AR/VR
