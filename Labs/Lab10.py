"""
    ***In all labs, students are expected to use Scratch code creator/emulator
    on CodeBug's website in order to understand the logic of the program, before they run it.

    In this lab students will learn about Classes and put all test their programming skills.
"""
import os
import sys
import picamera
import random
import time
import codebug_i2c_tether
import RPi.GPIO as GPIO

#Set up the GPIO Pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)

codebug=codebug_i2c_tether.CodeBug()
codebug.open()
codebug.clear()

#Q1 Create your own Codebug class called Bug. Have three variables called name,
#age and face. Create a function called getName (print out the name of the Bug),
#getAge(print age on LED arrray) and getFace (Which will show the face of the codebug
#on the LED grid). Make sure you have a constructor which will initialize the
#name, age and face of the Bug

class Bug:
    name=""
    age=0

    def __init__(self,name,age,face):
        self.name=name
        self.age=age
        self.face=face

    def getName(self):
        for letter in self.name:
            codebug.clear()
            codebug.write_text(0,0,letter)
            time.sleep(.5)
            
    def getAge(self):
        for letter in str(self.age):
            codebug.clear()
            codebug.write_text(0,0,letter)
            time.sleep(.5)
        
    def getFace(self):
        if(self.face=="happy"):
            codebug.set_row(4, 0b01010)
            codebug.set_row(3, 0b01010)
            codebug.set_row(2, 0b00000)
            codebug.set_row(1, 0b10001)
            codebug.set_row(0, 0b01110)
        elif(self.face=="sad"):
            codebug.set_row(4, 0b01010)
            codebug.set_row(3, 0b01010)
            codebug.set_row(2, 0b00000)
            codebug.set_row(1, 0b01110)
            codebug.set_row(0, 0b10001)
        else:
            codebug.set_row(4, 0b01010)
            codebug.set_row(3, 0b01010)
            codebug.set_row(2, 0b00000)
            codebug.set_row(1, 0b11111)
            codebug.set_row(0, 0b00000)

bug = Bug("Bob",21,"Happy")
bug.getName()
time.sleep(2)
codebug.clear()

bug.getAge()
time.sleep(2)
codebug.clear()

bug.getFace()
time.sleep(2)
codebug.clear()

#Q2 ***HARD
#Create a class named SensorCam, inside have a variable called filanme
#and three functions, arrowLeft (printing out an arrow pointing top left),
#smile (printing a smiley face) and takePicture, which will take a picture
#using the PiCam, whenever the PIR sensor is set off. *Make usre you have an
#arming system, ie user will press a button when ready to activate the system. 

"""
class SensorCam:
    filename=""
    def __init__(self,filename):
        self.filename=filename
    
    def arrowLeft(self):
        codebug.set_row(4, 0b11100)
        codebug.set_row(3, 0b11000)
        codebug.set_row(2, 0b10100)
        codebug.set_row(1, 0b00010)
        codebug.set_row(0, 0b00001)
        time.sleep(1)
        codebug.clear()

    def smile(self):
        codebug.set_row(4, 0b01010)
        codebug.set_row(3, 0b01010)
        codebug.set_row(2, 0b00000)
        codebug.set_row(1, 0b10001)
        codebug.set_row(0, 0b01110)    

    #Take picture using the camera
    def takePicture(self):
        with picamera.PiCamera() as camera:
            camera.resolution=(1600,1200)
            #camera.start_preview() #Start camera preview, be careful though might crash the Pi
            time.sleep(1)
            while(GPIO.input(8) != 1 or codebug.get_input("A")==1):
                time.sleep(.1)
            camera.capture(self.filename)          

filename=input("What do you want the file to be called?\n")
filename=filename+".jpg" 
cam = SensorCam(filename) 

while(True):
    codebug.clear()
    cam.arrowLeft()
    if(codebug.get_input("A")==1):
        cam.smile()
        time.sleep(.2)
        cam.takePicture()

    time.sleep(.2)
"""
