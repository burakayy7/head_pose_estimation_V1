import cv2
import mediapipe as mp
import numpy as np

print(cv2.__version__)

width=640
height=480

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
#cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

pose=mp.solutions.pose.Pose(False, True, True, 0.95) #type: ignore
myDraw=mp.solutions.drawing_utils #type: ignore

eyeColor=(255,0,0)
eyeRadius=5
eyeThickness=-1

leftROI = []
rightROI = []

params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.minArea = 1500
detector = cv2.SimpleBlobDetector_create(params)

im_with_keypoints=[]

while True:
    ignore,  frame = cam.read()
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)#mediapipe requires RGB color

    results=pose.process(frameRGB)
    #print(results)
    landmarks=[]
    if results.pose_landmarks != None:
        for lm in results.pose_landmarks.landmark:
            landmarks.append((int(lm.x*width),int(lm.y*height))) 
        
        #cv2.circle(frame,landmarks[2],eyeRadius,eyeColor,eyeThickness)#in landmarks array, the 3rd slot(2nd index) is the center if left eye
        #cv2.circle(frame,landmarks[5],eyeRadius,eyeColor,eyeThickness)#in landmarks array, the 6rd slot(5nd index) is the center if right eye

        leftROI = frame[landmarks[2][1]-10:landmarks[2][1]+20,landmarks[2][0]-40:landmarks[2][0]+40]
        rightROI = frame[landmarks[5][1]-20:landmarks[5][1]+20,landmarks[5][0]-40:landmarks[5][0]+40]
        lowB=np.array([0,160,0])
        highB=np.array([179,255,40])
        lowB2=np.array([0,70,0])
        highB2=np.array([179,255,200])
        lhsv = cv2.cvtColor(leftROI,cv2.COLOR_BGR2HSV)
        rhsv = cv2.cvtColor(rightROI,cv2.COLOR_BGR2HSV)
        myMaskLeye=cv2.inRange(lhsv,lowB,highB)
        myMaskReye=cv2.inRange(rhsv,lowB,highB)
        myMaskL=cv2.inRange(lhsv,lowB2,highB2)
        #keypoints = detector.detect(myMaskL)
        #im_with_keypoints = cv2.drawKeypoints(leftROI, keypoints, myMask, (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


        
        



        #cv2.imshow("Keypoints", im_with_keypoints)
        cv2.imshow("L2",myMaskL)
        cv2.moveWindow("L2",width+300,0)
        cv2.imshow("L",myMaskLeye)
        cv2.moveWindow("L",width+150,0)
        cv2.imshow("R",myMaskReye)
        cv2.moveWindow("R",width+150,100)
        cv2.imshow("Left ROI", leftROI)
        cv2.moveWindow("Left ROI", width, 0)
        cv2.imshow("Right ROI", rightROI)
        cv2.moveWindow("Right ROI",width,80)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()