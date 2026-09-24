import math


def joint_angle(a, b, c) -> float:
    """Return angle ABC in degrees for 2D/3D points."""
    ax, ay = float(a[0]), float(a[1])
    bx, by = float(b[0]), float(b[1])
    cx, cy = float(c[0]), float(c[1])
    v1 = (ax - bx, ay - by)
    v2 = (cx - bx, cy - by)
    n1 = math.hypot(*v1)
    n2 = math.hypot(*v2)
    if n1 == 0 or n2 == 0:
        return float("nan")
    cos_theta = max(-1.0, min(1.0, (v1[0] * v2[0] + v1[1] * v2[1]) / (n1 * n2)))
    return math.degrees(math.acos(cos_theta))


def ergonomic_screening_score(keypoints) -> int:
    """Simple transparent posture-risk screen, not a full official REBA calculation.

    Expected COCO keypoints: shoulders 5/6, hips 11/12, knees 13/14.
    The score is intended for portfolio/demo screening and must not be treated as
    an occupational-health assessment.
    """
    if keypoints is None or len(keypoints) < 15:
        return 0
    left = joint_angle(keypoints[5], keypoints[11], keypoints[13])
    right = joint_angle(keypoints[6], keypoints[12], keypoints[14])
    angles = [x for x in (left, right) if not math.isnan(x)]
    if not angles:
        return 0
    deviation = sum(abs(180.0 - x) for x in angles) / len(angles)
    if deviation < 15:
        return 1
    if deviation < 30:
        return 2
    if deviation < 45:
        return 3
    return 4
