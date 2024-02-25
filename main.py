import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
hands = mp.solutions.hands.Hands(max_num_hands=2)
draw = mp.solutions.drawing_utils

while True:
    #Закрытие окна
    if cv2.waitKey(1) & 0xFF == 27:
        break

    success, image = cap.read() 
    image = cv2.flip(image, 1)
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
    results = hands.process(imageRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

            draw.draw_landmarks(image, handLms, mp.solutions.hands.HAND_CONNECTIONS) #Рисуем ладонь

    cv2.imshow("Hand", image) 

# TODO
# - разбить поле камеры на 2 отдельных (для каждой руки)
# - считывать движения рук в каждом поле
#
# ____________________
# |--|↑|---||--|↑|---|
# |--------||--------|
# ||←|--|→||||←|--|→||
# |--------||--------|
# |--|↓|---||--|↓|---|
# |________||________|