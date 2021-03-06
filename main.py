import cv2
import numpy as np
import time
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkinter.ttk import Frame
from PIL import ImageTk, Image

white 		= "#FF0000"
lightBlue2 	= "#adc5ed"
font 		= "Constantia"
fontButtons = (font, 12)
maxWidth  	= 800
maxHeight 	= 480

#Graphics window
mainWindow = tk.Tk()
mainWindow.configure(bg=lightBlue2)
mainWindow.geometry('%dx%d+%d+%d' % (maxWidth,maxHeight,0,0))
mainWindow.resizable(0,0)
# mainWindow.overrideredirect(1)

mainFrame = Frame(mainWindow)
mainFrame.place(x=20, y=20)                

#Capture video frames
lmain = tk.Label(mainFrame)
lmain.grid(row=0, column=0)

cap = cv2.VideoCapture(0)

def show_frame():
	ret, frame = cap.read()

	cv2image   = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

	img   = Image.fromarray(cv2image).resize((760, 400))
	imgtk = ImageTk.PhotoImage(image = img)
	lmain.imgtk = imgtk
	lmain.configure(image=imgtk)
	lmain.after(10, show_frame)

closeButton = tk.Button(mainWindow, text = "CLOSE", font = fontButtons, bg = white, width = 20, height= 1)
closeButton.configure(command= lambda: mainWindow.destroy())              
closeButton.place(x=270,y=430)

# Keep track of the button state on/off 
#global is_stop 
is_stop = True
  
# Create Label 
my_label = tk.Label(mainWindow,  
    text = "Welcome to PiRecorder!!",  
    fg = "green",  
    font = ("Helvetica", 32)) 
  
my_label.pack(pady = 20) 
  
# Define our switch function 
def switch(): 
    global is_stop 
      
    # Determin is on or off 
    if is_stop: 
        stop_button.config(image = stop) 
        my_label.config(text = "Recording",  
                        fg = "grey") 
        is_stop = False
    else: 
        
        stop_button.config(image = record) 
        my_label.config(text = "Stopped", fg = "green") 
        is_stop = True
  
# Define Our Images 
record = tk.PhotoImage(file = "images/record.png") 
stop = tk.PhotoImage(file = "images/stop.png") 
  
# Create A Button 
stop_button = tk.Button(mainWindow, image = record, bd = 0, 
                   command = switch) 
stop_button.pack(pady = 50) 

show_frame()  #Display
mainWindow.mainloop()  #Starts GUI


