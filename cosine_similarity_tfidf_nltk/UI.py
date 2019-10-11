from tkinter import *
import cv2
import random 
import numpy as np
from tkinter import filedialog

root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

theLabel = Label(topFrame, text="OBJECT DETECTION", font="40", fg="lightgreen")
theLabel.pack()

w = Canvas(root, width=40, height=60) 
w.pack() 
canvas_height=20
canvas_width=300
y = int(canvas_height / 2) 
w.create_line(0, y, canvas_width, y ) 

def VIDEO():
  
     cap = cv2.VideoCapture(0)
# Check if the webcam is opened correctly
     if not cap.isOpened():
        raise IOError("Cannot open webcam")
     while True:
         ret, frame = cap.read()
         frame = cv2.resize(frame, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)
         cv2.imshow('Cam ', frame)
         c = cv2.waitKey(1)
         if c == ord('q'):
            break
     cv2.destroyAllWindows()
     cap.release()
	 
def OPEN():

     path=filedialog.askopenfilename(filetypes=[("Image File",'.jpg')])
     im = Image.open(path)
     tkimage = ImageTk.PhotoImage(im)
     myvar=Label(root,image = tkimage,width="500",height="500")
     myvar.image = tkimage
     myvar.pack()
	 
button = Button(root, text="Choose file", fg="blue", command=OPEN)
buttonCam = Button(root, text="Start camera", fg="blue", command=VIDEO)
button.pack()
buttonCam.pack()

 
root.mainloop()
