import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    success,img = cap.read()
    hands, img = detector.findHands(img, flipType=False) # with draw
    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        center1 = hand1["center"]

        if len(hands) == 2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]
            center2 = hand2["center"]
            distance, info, img = detector.findDistance(lmList1[8], lmList2[8], img)
    cv2.imshow("Image", img)
    cv2.waitKey(1)