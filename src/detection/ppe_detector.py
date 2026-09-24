from dataclasses import dataclass
from pathlib import Path
from typing import List

from ultralytics import YOLO


@dataclass
class Detection:
    class_id: int
    label: str
    confidence: float
    xyxy: tuple[float, float, float, float]


class PPEDetector:
    """Thin wrapper around an Ultralytics object-detection model."""

    def __init__(self, weights: str | Path, conf: float = 0.35):
        self.model = YOLO(str(weights))
        self.conf = conf

    def predict(self, frame) -> List[Detection]:
        result = self.model.predict(frame, conf=self.conf, verbose=False)[0]
        names = result.names
        detections: List[Detection] = []
        if result.boxes is None:
            return detections
        for box in result.boxes:
            cls = int(box.cls.item())
            conf = float(box.conf.item())
            x1, y1, x2, y2 = [float(v) for v in box.xyxy[0].tolist()]
            detections.append(Detection(cls, str(names[cls]), conf, (x1, y1, x2, y2)))
        return detections
