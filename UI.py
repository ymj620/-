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
#try:
#    while True:
#        p.ChangeDutyCycle(0)
#        print "angle : 0 "
#        time.sleep(1)
#        p.ChangeDutyCycle(10)
#        print "angle : 20 "
#        time.sleep(1)
#        p.ChangeDutyCycle(45)
#        print "angle : 90 "
#        time.sleep(1)
        
#except KeyboardInterrupt:
#    p.stop()
#GPIO.cleanup()

now = datetime.now()
top = TK.Tk()
var = IntVar()
#var0  = StringVar()
#label0 = Label(top, textvariable=var,relief = RAISED)

capture = 30
servo0 = 0

def helloCallBack():
    tkMessageBox.showinfo("Hello Python","Hello World")

    
def donothing():
    filewin = Toplevel(top)
    button = Button(filewin,text="Do nothing button")
    button.pack()
    
def setting0():
    selection = "You need to select options" + str(var.get())
    label.config(text = selection)
    R1 = Radiobutton(top,text="Option 1", variable=var,value=1,command=sel)
    R2 = Radiobutton(top,text="Option 2", variable=var,value=2,command=sel)
    R3 = Radiobutton(top,text="Option 3", variable=var,value=3,command=sel)
    R1.pack( anchor = W )
    R2.pack( anchor = W )
    R3.pack( anchor = W )

    label = Label(top)
    label.pack()
    
def openServo():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin,GPIO.OUT)
    p=GPIO.PWM(pin,50)
    p.start(0)
    global servo0
    time.sleep(1)
    p.ChangeDutyCycle(45)
    time.sleep(3)
    print "angle : O "
#    time.sleep(5)
#    p.stop()
    servo0=0
    p.stop()
    GPIO.cleanup()
    
def closeServo():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin,GPIO.OUT)
    p=GPIO.PWM(pin,50)
    p.start(0)
    global servo0
    time.sleep(1)
    p.ChangeDutyCycle(0)
    time.sleep(3)
    print "angle : C "
    servo0=1
    p.stop()
    GPIO.cleanup()
    
def exitAndCleanup():
    GPIO.cleanup()
    top.quit();
    
    #filename = PhotoImage(file = "sunshine.gif")


C = TK.Canvas(top,bg="white",height=480,width=800)

#image = C.create_image(50,50,anchor=NE,image=filename)
oval = C.create_polygon(0,0,640,0,640,480,0,480, fill="red")


B1 = TK.Button(top,text = "History", command = helloCallBack)#openServo)
B2 = TK.Button(top,text = "Capture", command = helloCallBack)#closeServo)
B3 = TK.Button(top,text = "Training", command = helloCallBack)
B4 = TK.Button(top,text = "Setting", command = setting0)
B5 = TK.Button(top,text = "Exit", command = exitAndCleanup)

B1.pack()
B1.place(x=640,y=0,height=120,width=160)
B2.pack()
B2.place(x=640,y=120,height=120,width=160)
B3.pack()
B3.place(x=640,y=240,height=120,width=160)
B4.pack()
B4.place(x=640,y=360,height=120,width=80)
B5.pack()
B5.place(x=720,y=360,height=120,width=80)
C.pack()

top.attributes("-fullscreen",True)
top.title("Recognizer")
top.resizable(False,False)
top.bind("<F11>",lambda event : top.attributes("-fullscreen" , not top.attributes("-fullscreen")))
top.bind("<Escape>",lambda event : top.attributes("-fullscreen",False))

#menubar = Menu(top)
#fm = Menu(menubar,tearoff=0)
#fm.add_command(label="New",command=donothing)

#fm.add_separator()

#fm.add_command(label="Exit",command=top.quit)
#menubar.add_cascade(label="File",menu=fm)

#em = Menu(menubar,tearoff=0)
#em.add_command(label="Undo", command=donothing)
#em.add_command(label="Redo", command=donothing)
#em.add_separator()
#em.add_command(label="Cut", command=donothing)

#menubar.add_cascade(label="Edit",menu=em)
#hm=Menu(menubar,tearoff=0)
#hm.add_command(label="Help Index", command=donothing)
#menubar.add_cascade(label="Help",menu=hm)

#top.config(menu=menubar)

#var0.set("Now")
#label0.pack
#label0.place(x=50,y=450)
print(now)
top.mainloop()