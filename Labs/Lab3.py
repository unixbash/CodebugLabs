"""
    ***In all labs, students are expected to use Scratch code creator/emulator
    on CodeBug's website in order to understand the logic of the program, before they run it.

    In this lab students will learn loops, while and for
"""
import random
import time
import codebug_i2c_tether

codebug=codebug_i2c_tether.CodeBug()
codebug.open()
codebug.clear()

#Q1 function given to the student
def randNumber():
    rand=random.randint(1,9)
    codebug.write_text(0,0,str(rand))
    return rand

#Q1 Write a program that will check whether the number on the CodeBug is
#odd or even, if odd print "Odd!" or if even, print "Even!"
#Hint: use the % operator
"""
randomNumber=randNumber()#Given

if(randomNumber % 2 == 0):
    print("Even!")
else:
    print("Odd!")
"""
    
#Q2 Write a program that will check which button is being pushed by the user.
#Make sure you sleep for two seconds, before you check and use indicate buttons
#pressed using arrows on the LED grid, ie. if A is pressed have a left pointing
#arrow, if both are pressed, point the arrow upwards.
#HINT: use codebug.get_input('A') to check which button was pressed

time.sleep(2)
if(codebug.get_input('A') and codebug.get_input('B')):
    codebug.set_row(4, 0b00100)
    codebug.set_row(3, 0b01110)
    codebug.set_row(2, 0b00100)
    codebug.set_row(1, 0b00100)
    codebug.set_row(0, 0b00100)
elif(codebug.get_input('A')):
    codebug.set_row(4, 0b11100)
    codebug.set_row(3, 0b11000)
    codebug.set_row(2, 0b10100)
    codebug.set_row(1, 0b00010)
    codebug.set_row(0, 0b00001)
elif(codebug.get_input('B')):
    codebug.set_row(4, 0b00111)
    codebug.set_row(3, 0b00011)
    codebug.set_row(2, 0b00101)
    codebug.set_row(1, 0b01000)
    codebug.set_row(0, 0b10000)

