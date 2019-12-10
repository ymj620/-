import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import numpy as np
import os
from PIL import Image
import time
import RPi.GPIO as GPIO

pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)
p=GPIO.PWM(pin,50)
p.start(0)
cnt=0

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascades/haarcascade_frontalface_default.xml"
eyeCascade = cv2.CascadeClassifier("haarcascades/haarcascade_eye.xml")
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX

time.sleep(0.1)

id = 0
names = ['none', 'JH.L', 'Subin.L', 'SI.L', 'HJ.L']

cam = PiCamera()
cam.resolution = (640, 480)
cam.framerate = 32
rawCapture = PiRGBArray(cam, size=(640, 480))
minW = 0.1*640
minH = 0.1*480

detect=0

servo=0

for frame in cam.capture_continuous(rawCapture, format="bgr" , use_video_port=True):

    ret = frame.array
    img = frame.array
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    
    vis = img
    
    if detect == 0 :
        faces = faceCascade.detectMultiScale(gray,
            scaleFactor=1.2, minNeighbors=5,minSize=(20,20))
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            detect=1

            eyes = eyeCascade.detectMultiScale(roi_gray, scaleFactor= 1.5, minNeighbors=10, minSize=(5, 5))
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color, (ex,ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    else :
        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
           )

        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            # Check if confidence is less them 100 ==> "0" is perfect match
            if (confidence < 60):
                id = names[id]
                confidence = "  {0}%".format(round(130 - confidence))
                servo=1
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(130 - confidence))
        
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('image', vis)
        
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
# clear the stream in preparation for the next frame

# if the 'q' key was pressed, break from the loop

    if key == ord("q"):
        GPIO.cleanup()
        break


    if servo == 1 :
        p.ChangeDutyCycle(2)
        time.sleep(1)
        print "angle : Open "
        time.sleep(4)
        p.start(0)
        time.sleep(1)
        p.ChangeDutyCycle(50)
        time.sleep(1)
        print "angle : Close "
        p.stop()

        servo=0
        time.sleep(1)
















