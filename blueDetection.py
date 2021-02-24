import cv2
import numpy as np
import serial

# lowerBound = np.array([33, 80, 40]) #Green Color Bounds
# upperBound = np.array([102, 255, 255])

# lowerBound = np.array([110, 50, 50])  # Blue COlor Bounds
# upperBound = np.array([130, 255, 255])
arduinoCom = serial.Serial('COM8', 115200, timeout=.1)
lowerBound = np.array([0, 0, 212])  # White Color Bounds
upperBound = np.array([131, 255, 255])

font = cv2.FONT_HERSHEY_SIMPLEX
cam = cv2.VideoCapture(0)
kernelOpen = np.ones((5, 5))
kernelClose = np.ones((20, 20))

while True:
    ret, img = cam.read()
    img = cv2.resize(img, (340, 220))

    # convert BGR to HSV
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # create the Mask
    mask = cv2.inRange(imgHSV, lowerBound, upperBound)
    # morphology
    maskOpen = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernelOpen)
    maskClose = cv2.morphologyEx(maskOpen, cv2.MORPH_CLOSE, kernelClose)

    maskFinal = maskClose
    conts, h = cv2.findContours(maskFinal.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(img, conts, -1, (255, 0, 0), 3)
    for i in range(len(conts)):
        x, y, w, h = cv2.boundingRect(conts[i])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        # cv2.PutText(cv2.fromarray(img), str(i + 1), (x, y + h), font, (0, 255, 255))
        cv2.putText(img, str(i + 1), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)
    if len(conts) > 1:
        print('Running')
        arduinoCom.write(str.encode('1'))
    else:
        print('Not Running')
        arduinoCom.write(str.encode('0'))
    cv2.imshow("maskClose", maskClose)
    cv2.imshow("maskOpen", maskOpen)
    cv2.imshow("mask", mask)
    cv2.imshow("cam", img)

    cv2.waitKey(10)
