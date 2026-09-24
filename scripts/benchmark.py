import argparse
import time
import cv2

from src.detection.pose_detector import PoseDetector


def main():
    parser = argparse.ArgumentParser(description="Benchmark pose inference")
    parser.add_argument("--source", required=True)
    parser.add_argument("--pose-model", required=True)
    parser.add_argument("--frames", type=int, default=100)
    args = parser.parse_args()

    source = int(args.source) if args.source.isdigit() else args.source
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        raise RuntimeError(f"Could not open source: {args.source}")
    model = PoseDetector(args.pose_model)

    count = 0
    start = time.perf_counter()
    while count < args.frames:
        ok, frame = cap.read()
        if not ok:
            break
        model.predict(frame)
        count += 1
    elapsed = time.perf_counter() - start
    cap.release()

    if count == 0:
        raise RuntimeError("No frames processed")
    print(f"Frames: {count}")
    print(f"Elapsed: {elapsed:.3f}s")
    print(f"FPS: {count / elapsed:.2f}")
    print(f"Latency: {(elapsed / count) * 1000:.2f} ms/frame")


if __name__ == "__main__":
    main()
