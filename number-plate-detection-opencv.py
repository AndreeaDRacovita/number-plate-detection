# OpenCV Tutorial from Murtaza's Workshop - Robotics and AI

import numpy as np
import cv2

num_plate_cascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")

width = 640
height = 480
min_area = 500
color = (255, 0, 255)
count = 0

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, width)
cap.set(4, height)
cap.set(10, 150)

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    num_plate = num_plate_cascade.detectMultiScale(imgGray, 1.1, 10)
    for (x, y, w, h) in num_plate:
        area = w * h
        if area > min_area:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                        1, color, 2)
            img_roi = img[y:y+h, x:x+w]
            cv2.imshow("Number Plate", img_roi)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                cv2.imwrite("NoPlate_" + str(count) + ".jpg", img_roi)
                count += 1

    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
