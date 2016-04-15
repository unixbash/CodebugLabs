"""
    ***In all labs, students are expected to use Scratch code creator/emulator
    on CodeBug's website in order to understand the logic of the program, before they run it.

    In this lab students will learn how to write and use functions
"""

import time
import codebug_i2c_tether

codebug=codebug_i2c_tether.CodeBug()
codebug.open()
codebug.clear()


#Q1 Write a simple function that will flash all leds and put it in a loop that
#will repeat that process 5 times.
#***You can see how much code repetition we can avoid in our programs by using functions 

"""
def flash():
    codebug.set_row(0,0b11111)
    codebug.set_row(1,0b11111)
    codebug.set_row(2,0b11111)
    codebug.set_row(3,0b11111)
    codebug.set_row(4,0b11111)
    time.sleep(.5)
    codebug.clear()
    time.sleep(.5)

for i in range(0,5):
    flash()
"""

#Q2 Create a function that will take in the given list of integers and
#print them on the CodeBug.
"""
def printList(userList):
    for n in userList:
        codebug.clear()
        codebug.write_text(0,0,str(n))
        time.sleep(1)

num=[8,0,6,2,1,3,5,7,9,4]
printList(num)
"""

#Q3 Write a functions  that will take three inputs, button, shape and time.
#This function will print one of the 3 available shapes, when the user presses
#the button supplied and for the duration in seconds given
#***Hint: You might want to create three separate functions to display the spahes
#this will make you code much cleaner and easier to debug.
"""
def shape1(t):
    codebug.set_row(4,0b01010)
    codebug.set_row(3,0b01010)
    codebug.set_row(2,0b00000)
    codebug.set_row(1,0b10001)
    codebug.set_row(0,0b01110)
    time.sleep(t)
    codebug.clear()
def shape2(t):
    codebug.set_row(4,0b01010)
    codebug.set_row(3,0b00000)
    codebug.set_row(2,0b11111)
    codebug.set_row(1,0b10001)
    codebug.set_row(0,0b01110)
    time.sleep(t)
    codebug.clear()
def shape3(t):
    codebug.set_row(4,0b01010)
    codebug.set_row(3,0b11111)
    codebug.set_row(2,0b11111)
    codebug.set_row(1,0b01110)
    codebug.set_row(0,0b00100)
    time.sleep(t)
    codebug.clear()

def blinkShape(button, shape, time):
    if(codebug.get_input(button)==1):
        if(shape==1):
            shape1(time)
        elif(shape==2):
            shape2(time)
        elif(shape==3):
            shape3(time) 
        else:
            print("Invlaid shape number!")
while(True):
    
    blinkShape("A",3,1)
    time.sleep(.1)
"""
