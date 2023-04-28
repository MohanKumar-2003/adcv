import cv2
import mediapipe as mp
import time
import HandTrackingModule as ht

p_time = 0
c_time = 0
cap = cv2.VideoCapture(0)
detector = ht.handDetector()
while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmsList=detector.findPosition(img)
        if len(lmsList)!=0:
            print(lmsList[4])
        c_time = time.time()
        fps = 1 / (c_time - p_time)
        p_time = c_time
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)
