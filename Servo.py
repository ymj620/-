# -*- coding: utf-8 -*-
import Tkinter as TK
from Tkinter import *
import tkMessageBox
from datetime import datetime
import time
import RPi.GPIO as GPIO

pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)
p=GPIO.PWM(pin,50)
p.start(0)
cnt=0


now = datetime.now()
root = TK.Tk()
var = IntVar()
#var0  = StringVar()
#label0 = Label(top, textvariable=var,relief = RAISED)
capture = 30

p.ChangeDutyCycle(2)
time.sleep(1)
print "angle : Open "
time.sleep(5)
p.start(0)
time.sleep(1)
p.ChangeDutyCycle(50)
time.sleep(1)
print "angle : Close "
p.stop()

GPIO.cleanup()


