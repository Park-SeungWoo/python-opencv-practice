import cv2

cap = cv2.VideoCapture('videos/arduino.mp4')
# codec = cv2.Videowriter_fourcc('M', 'J', 'P', 'G')
# out = cv2.VideoWriter('videos/output.avi', codec, 25.0, (640, 480))
out = cv2.VideoWriter('videos/output2.mp4', cv2.VideoWriter_fourcc(*'MJPG'), 25, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        frame = cv2.flip(frame, 1)
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(100) & 0xFF == 27:
            break


cap.release()
out.release()
cv2.destroyAllWindows()