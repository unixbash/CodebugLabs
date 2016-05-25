import os
import sys
import time
import picamera
import codebug_i2c_tether
import RPi.GPIO as GPIO

#Set up the GPIO Pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)

def arrowLeft():
    codebug.set_row(4, 0b11100)
    codebug.set_row(3, 0b11000)
    codebug.set_row(2, 0b10100)
    codebug.set_row(1, 0b00010)
    codebug.set_row(0, 0b00001)
    time.sleep(1)
    codebug.clear()

def smile():
    codebug.set_row(4, 0b01010)
    codebug.set_row(3, 0b01010)
    codebug.set_row(2, 0b00000)
    codebug.set_row(1, 0b10001)
    codebug.set_row(0, 0b01110)    

#Take picture using the camera
def takePicture(filename):
    with picamera.PiCamera() as camera:
        camera.resolution=(1600,1200)
        camera.start_preview()
        time.sleep(1)
        while(GPIO.input(12) != 1):
            time.sleep(.1)
        camera.capture(filename)


if __name__ == '__main__':
    with codebug_i2c_tether.CodeBug() as codebug:
        
        while(True):
            codebug.clear()
            arrowLeft()
            if(codebug.get_input("A")==1):
                smile()
                time.sleep(.2)
                takePicture("hello.jpg")

            time.sleep(.2)
