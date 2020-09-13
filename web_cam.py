import cv2

cap = cv2.VideoCapture(0)
cap.set(4, 270)
cap.set(3, 340)
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()