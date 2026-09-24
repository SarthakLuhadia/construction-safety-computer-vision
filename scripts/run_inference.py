import argparse
from pathlib import Path
import cv2

from src.detection.ppe_detector import PPEDetector
from src.detection.pose_detector import PoseDetector
from src.inference.pipeline import SafetyPipeline


def main():
    parser = argparse.ArgumentParser(description="Construction safety CV inference")
    parser.add_argument("--source", required=True, help="Video path or webcam index")
    parser.add_argument("--ppe-model", required=True)
    parser.add_argument("--pose-model", required=True)
    parser.add_argument("--conf", type=float, default=0.35)
    parser.add_argument("--output", default="outputs/result.mp4")
    args = parser.parse_args()

    source = int(args.source) if args.source.isdigit() else args.source
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        raise RuntimeError(f"Could not open source: {args.source}")

    ppe = PPEDetector(args.ppe_model, args.conf)
    pose = PoseDetector(args.pose_model, args.conf)
    pipeline = SafetyPipeline(ppe, pose)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) or 1280)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) or 720)
    fps = cap.get(cv2.CAP_PROP_FPS) or 25.0
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    writer = cv2.VideoWriter(args.output, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))

    while True:
        ok, frame = cap.read()
        if not ok:
            break
        annotated, _ = pipeline.process(frame)
        writer.write(annotated)
        cv2.imshow("Construction Safety CV", annotated)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    writer.release()
    cv2.destroyAllWindows()
    print(f"Saved output to {args.output}")


if __name__ == "__main__":
    main()
