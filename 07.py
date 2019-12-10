from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import os

camera = PiCamera()

camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

face_detector = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id

face_id = input('\n enter user id end press <return> ==>  ')
print("\n [INFO] Initializing face capture. Look the camera and wait ...")

# Initialize individual sampling face count
count = 0
pictures = 30


for frame in camera.capture_continuous(rawCapture, format="bgr" , use_video_port=True):
    ret = frame.array
    img = frame.array
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    
    vis = img
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1

        vis = img.copy()
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
    cv2.imshow('image', vis)
    
    if count >= pictures: # Take 30 face sample and stop video
         break
        
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
# clear the stream in preparation for the next frame

# if the 'q' key was pressed, break from the loop

    if key == ord("q"):
        break


# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
