"""
    ***In all labs, students are expected to use Scratch code creator/emulator
    on CodeBug's website in order to understand the logic of the program, before they run it.

    In this lab students will learn about Python File I/O
"""
import os
import sys
import picamera
import random
import time
import codebug_i2c_tether

codebug=codebug_i2c_tether.CodeBug()
codebug.open()
codebug.clear()

#Q1 Read in a text file and there will be a single integer,
#represent that integer on the CodeBug LED display.

"""
file = open("num.txt","r+")
num = file.read(1)

codebug.write_text(0,0,str(num))
file.close
"""

#Q2 Create a number counter, that will flash an LED every time you press a
#button on the CodeBug and increment a counter, when the user presses the other
#button all LEDs should flash and the result of the count should be saved in a
#text file called counted.txt

"""
counter=0

while(codebug.get_input('A') != 1):
    codebug.clear()
    if(codebug.get_input('B')==1):
        counter+=1
        codebug.set_pixel(2,2,1)
        time.sleep(0.2)
    time.sleep(0.1)
    
codebug.set_row(2,0b11111)
time.sleep(0.2)
codebug.clear()

with open("counted.txt","w") as resultF:
    print(format(counter), file=resultF)
"""

#Q3 Create a program that will take a picture using the PiCamea when a button on
#the Codebug is pressed. Make the image file name the current date and time.

"""
with picamera.PiCamera() as camera:
    camera.resolution=(1600,1200)
    camera.start_preview()
    time.sleep(1)
    while(codebug.get_input('A') != 1):
        time.sleep(.1)
    filename=time.strftime("%H-%M--%d-%m-%Y")+".jpg"
    print (filename)
    camera.capture(filename)
"""
