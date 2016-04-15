"""
    ***In all labs, students are expected to use Scratch code creator/emulator
    on CodeBug's website in order to understand the logic of the program, before they run it.

    In this lab students will learn about searching throught lists and there will be
    a bonus question at the end of the lab testing their programming skills.
"""
import random
import time
import codebug_i2c_tether

codebug=codebug_i2c_tether.CodeBug()
codebug.open()
codebug.clear()

#Q1 Create a program whitch will ask the user to guess whether a number exist
#in a list of 10 randomly generated elements. Your program should print
#the index of the position where that value occurs (on the codebug), otherwise
#tell the user, value not found by drawing an X on the CodeBug
#Hint: to make your code cleaner, write two functions one displaying X and
#the other creating a list of 10 randomly generated number 0-50

def drawX():
    codebug.set_row(4,0b10001)
    codebug.set_row(3,0b01010)
    codebug.set_row(2,0b00100)
    codebug.set_row(1,0b01010)
    codebug.set_row(0,0b10001)
def generateList():
    num=[]
    for i in range(0,10):
        num.append(random.randint(0,50))
    return num

guess=input("Guess a number from 0 to 50:\n")
num=generateList()
n=0
print(num)
while(n < len(num)):
    if(num[n]==int(guess)):
        codebug.write_text(0,0,str(n))
    n+=1
    if(n == len(num)):
        drawX()
    
  
