import time
import cv2

from src.utils.visualization import draw_detections, draw_pose
from src.ergonomics.reba import ergonomic_screening_score


class SafetyPipeline:
    def __init__(self, ppe_detector=None, pose_detector=None):
        self.ppe_detector = ppe_detector
        self.pose_detector = pose_detector

    def process(self, frame):
        start = time.perf_counter()
        detections = self.ppe_detector.predict(frame) if self.ppe_detector else []
        persons = self.pose_detector.predict(frame) if self.pose_detector else []
        frame = draw_detections(frame, detections)
        frame = draw_pose(frame, persons)
        for person in persons:
            score = ergonomic_screening_score(person.xy)
            x1, y1, _, _ = map(int, person.bbox)
            cv2.putText(frame, f"Ergo screen: {score}/4", (x1, max(40, y1 - 28)), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 200, 255), 2)
        elapsed = time.perf_counter() - start
        fps = 1.0 / elapsed if elapsed > 0 else 0.0
        cv2.putText(frame, f"Pipeline FPS: {fps:.1f}", (10, 28), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        return frame, fps
