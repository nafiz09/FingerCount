import cv2
import mediapipe as mp
import HTModule as htm

cap = cv2.VideoCapture(1)
det = htm.HandDetector(detCon=0.9,tracCon=0.9)
tips = [4,8,12,16,20]

while True:
    suc, img = cap.read()
    width = 1080
    height = 720
    dim = (width, height)
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    img = cv2.flip(img,1)
    img = det.FindHands(img,draw=0)
    lmlist = det.FindPosition(img,draw = False)
    if len(lmlist)!=0:
        fingers = []
        if lmlist[tips[4]][1] > lmlist[tips[0]][1]:
            if lmlist[tips[0]][1] < lmlist[tips[0] - 2][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            for id in range(1,5):
                if lmlist[tips[id]][2]<lmlist[tips[id]-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            h, w, c = img.shape
            #cv2.rectangle(img,(630,370),(580,450),(0,0,0),cv2.FILLED)
            cv2.putText(img,str(fingers.count(1)),(w-50,h-50),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),6)
            print(fingers.count(1))

        else:
            if lmlist[tips[0]][1] > lmlist[tips[0] - 2][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            for id in range(1,5):
                if lmlist[tips[id]][2]<lmlist[tips[id]-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            h, w, c = img.shape
            #cv2.rectangle(img,(630,370),(580,450),(0,0,0),cv2.FILLED)
            cv2.putText(img,str(fingers.count(1)),(w-50,h-50),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),6)
            print(fingers.count(1))

    #img  = cv2.flip(img,2)
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break