from dataclasses import dataclass
from pathlib import Path
from typing import List

from ultralytics import YOLO


@dataclass
class PosePerson:
    xy: object
    confidence: float
    bbox: tuple[float, float, float, float]


class PoseDetector:
    """YOLO pose inference wrapper."""

    def __init__(self, weights: str | Path, conf: float = 0.25):
        self.model = YOLO(str(weights))
        self.conf = conf

    def predict(self, frame) -> List[PosePerson]:
        result = self.model.predict(frame, conf=self.conf, verbose=False)[0]
        persons: List[PosePerson] = []
        if result.boxes is None or result.keypoints is None:
            return persons
        for i, box in enumerate(result.boxes):
            xy = result.keypoints.xy[i].cpu().numpy()
            confidence = float(box.conf.item())
            bbox = tuple(float(v) for v in box.xyxy[0].tolist())
            persons.append(PosePerson(xy, confidence, bbox))
        return persons
