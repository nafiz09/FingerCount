import cv2
import mediapipe as mp

class HandDetector():
    def __init__(self,mode = False,maxHands = 2,detCon = 0.5, tracCon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detCon = detCon
        self.tracCon = tracCon
        self.mp_hand = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils
        self.hand = self.mp_hand.Hands(self.mode,self.maxHands,self.detCon,self.tracCon)

    def FindHands(self,img,draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hand.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for lm in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(img, lm, self.mp_hand.HAND_CONNECTIONS)
        return img


    def FindPosition(self,img,HandNo = 0,draw = True):
        lmlist = []
        if self.results.multi_hand_landmarks:
            myhand = self.results.multi_hand_landmarks[HandNo]
            for id, l in enumerate(myhand.landmark):
                h, w, c = img.shape
                cx, cy = int(l.x * w), int(l.y * h)
                lmlist.append([id,cx,cy])
                if draw:
                    cv2.circle(img, (cx, cy), 10, (255, 255, 255), cv2.FILLED)

        return lmlist


def main():
    cap = cv2.VideoCapture(1)
    det = HandDetector()
    while True:
        suc, img = cap.read()
        img = det.FindHands(img)
        lmlist = det.FindPosition(img)
        if len(lmlist)!=0:
            print(lmlist[8])
        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


if __name__ == "__main__":
    main()