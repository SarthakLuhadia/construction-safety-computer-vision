import cv2


def draw_detections(frame, detections):
    for d in detections:
        x1, y1, x2, y2 = map(int, d.xyxy)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 220, 0), 2)
        cv2.putText(frame, f"{d.label} {d.confidence:.2f}", (x1, max(20, y1 - 8)), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 220, 0), 2)
    return frame


def draw_pose(frame, persons):
    for person in persons:
        points = person.xy
        for x, y in points:
            if x > 0 and y > 0:
                cv2.circle(frame, (int(x), int(y)), 3, (255, 180, 0), -1)
        x1, y1, x2, y2 = map(int, person.bbox)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 180, 0), 1)
    return frame
