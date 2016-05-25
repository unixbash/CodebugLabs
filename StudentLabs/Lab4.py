"""
    ***In all labs, students are expected to use Scratch code creator/emulator
    on CodeBug's website in order to understand the logic of the program, before they run it.

    In this lab students will learn about loops
"""
import time
import codebug_i2c_tether
import RPi.GPIO as GPIO

codebug=codebug_i2c_tether.CodeBug()
codebug.open()
codebug.clear()

#Pre set GPIO Pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)


#Q1 Using a loop, display numbers from 0 to 9 on the LED matrix.
#The duration of each number showing will be 1 second.
"""
n=0

while(n < 10):
    codebug.clear()
    codebug.write_text(0,0,str(n))
    n=n+1
    time.sleep(1)
"""
#Q2 In this question, you need to use a for loop to print out every letter
#from a string provided to you by the user. (On the CodeBug)
"""
userInput=input("Please enter a string: \n")

for letter in userInput:
    codebug.clear()
    codebug.write_text(0,0,letter)
    time.sleep(.5)
"""

#Q3 Using the CodeBug and the PIR sensor, create a program that will blink all leds
# when the PIR sensor is triggered. Use a while loop to constantly listen out for sensor input
"""
while(True):
    if(GPIO.input(8) == 1):
        time.sleep(.5)
        codebug.set_row(4, 0b11111)
        codebug.set_row(3, 0b11111)
        codebug.set_row(2, 0b11111)
        codebug.set_row(1, 0b11111)
        codebug.set_row(0, 0b11111)
        time.sleep(.5)
        codebug.clear()
    time.sleep(.1)
"""   

#Q4 Using a nested loop, create a program that will eluminate a single pixel
#starting from 0,0 up to 5,5. For an example of the program running look at http://i.imgur.com/Yb9JdOI.gifv
"""
i=0
j=0

while(i < 5):
    while(j<5):
        codebug.set_pixel(j,i,1)
        time.sleep(.5)
        j=j+1
    j=0    
    i=i+1
"""

#Q5 In this question, you wiil put some of the skills you have learned to use, create a
#small game that will allow the user to move an LED in the middle of the matrix
#left or right using the two buttons. If you require any hints, look at the Drive game

position = 2
codebug.set_pixel(position,2,1)

while(True):

    if(codebug.get_input("A")==1):
        if(position > 0):
            codebug.set_pixel(position, 2, 0) 
            position -= 1
            codebug.set_pixel(position, 2, 1)

    if(codebug.get_input("B")==1):
        if(position < 4):
            codebug.set_pixel(position, 2, 0) 
            position += 1
            codebug.set_pixel(position, 2, 1)
  
    time.sleep(.2)


