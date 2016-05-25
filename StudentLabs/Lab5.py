"""
    ***In all labs, students are expected to use Scratch code creator/emulator
    on CodeBug's website in order to understand the logic of the program, before they run it.

    In this lab students will learn about Lists
"""
import time
import codebug_i2c_tether
import RPi.GPIO as GPIO

codebug=codebug_i2c_tether.CodeBug()
codebug.open()
codebug.clear()

#Q1 Using the given list of numbers from 0 to 9, print out even numbers on the CodeBug
"""
n=[0,1,2,3,4,5,6,7,8,9]

for i in n:
    codebug.clear()
    if(i%2==0):
        codebug.write_text(0,0,str(i))
    time.sleep(1)
"""

#Q2 Using a list and two for loops, parse the user input string and display each
#character on the CodeBug, this is similar to an excersise from the rpevious lab

"""
userInput=input("Please enter a string: \n")
charList=[''] #initialize to an empty list

for letter in userInput:
    charList.append(letter)

for char in charList:
    codebug.clear()
    codebug.write_text(0,0,char)
    time.sleep(.5)
"""

#***HARD*** Q3 Write a rpogram that will use the buttons on the CodeBug to
# iterate throught the given list and increment the current element, for example
# button A will increment the list iterator and button B will increment the value
# of that element in the list.

n=[0,0,0,0,0,0,0,0,0,0]
i=0
codebug.write_text(0,0,str(n[i]))

while(i < 10):
    
    if(codebug.get_input("A")==1):
        time.sleep(.5) #avoid setting off the next consition requiring A
        while(n[i] < 9 and codebug.get_input("A")!=1):
            if(codebug.get_input("B")==1):
                codebug.clear()
                n[i]+=1
                codebug.write_text(0,0,str(n[i]))
            time.sleep(.2)
        
        codebug.write_text(0,0,str(0))
        i+=1
    time.sleep(.1)
print(n)
