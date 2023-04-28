import cv2
cam = cv2.VideoCapture(0)
cam.set(3, 648)
cam.set(4, 488)
faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
    retV, frame = cam.read()
    abuabu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(abuabu, 1.3, 5)
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow('Face Detection',frame)
    #cv2.imshow('Face Detection 2',abuabu)
    k = cv2.waitKey(1) & 0xFF
    if k == 20 or k == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()