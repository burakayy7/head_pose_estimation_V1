import cv2
import numpy as np
import dlib
import math

# width=1280
# height=720
# cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
# cam.set(cv2.CAP_PROP_FPS, 30)
# cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("C:/Users/Burak-as-user/Documents/PythonSaves/pyAI3.6/Scripts/shape_predictor_68_face_landmarks.dat")




while True:
    _, frame = cam.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        cv2.rectangle(frame, (x1,y1), (x2, y2), (0,255,0),3)
        landmarks = predictor(gray, face)
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x,y),3,(255,0,0),-1)
        d = math.sqrt(math.pow(landmarks.part(31).x-landmarks.part(28).x,2)+math.pow(landmarks.part(31).y-landmarks.part(28).y,2))
        l = (150*6)/d
        print(l)


        

    cv2.imshow("F", frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
cam.release()