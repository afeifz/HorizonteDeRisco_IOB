import cv2
import time

camera = cv2.VideoCapture(0)

ret, frame1 = camera.read()
ret, frame2 = camera.read()

movement_avg = 0

current_risk = "LOW"
last_update = time.time()

while camera.isOpened():

    diff = cv2.absdiff(frame1, frame2)

    gray = cv2.cvtColor(
        diff,
        cv2.COLOR_BGR2GRAY
    )

    blur = cv2.GaussianBlur(
        gray,
        (5, 5),
        0
    )

    _, thresh = cv2.threshold(
        blur,
        50,
        255,
        cv2.THRESH_BINARY
    )

    movement = cv2.countNonZero(thresh)

    movement_avg = int(
        movement_avg * 0.8 +
        movement * 0.2
    )

    if time.time() - last_update > 1:

        if movement_avg > 20000:
            current_risk = "CRITICAL"
        elif movement_avg > 10000:
            current_risk = "MEDIUM"
        else:
            current_risk = "LOW"

        last_update = time.time()

    cv2.putText(
        frame1,
        f"RISK: {current_risk}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    cv2.putText(
        frame1,
        f"MOVEMENT: {movement_avg}",
        (20, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    bar_width = min(movement_avg // 200, 300)

    cv2.rectangle(
        frame1,
        (20, 120),
        (320, 150),
        (255, 255, 255),
        2
    )

    cv2.rectangle(
        frame1,
        (20, 120),
        (20 + bar_width, 150),
        (0, 255, 0),
        -1
    )

    cv2.imshow(
        "DisasterVision Monitor",
        frame1
    )

    frame1 = frame2
    ret, frame2 = camera.read()

    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()