"""
    ***In all labs, students are expected to use Scratch code creator/emulator
    on CodeBug's website in order to understand the logic of the program, before they run it.

    In this lab students will learn flow controll, mainly if statements
"""
import random
import time
import codebug_i2c_tether

codebug=codebug_i2c_tether.CodeBug()
codebug.open()
codebug.clear()

#Q4 function
def binaryToDecimal():
    rand=random.randint(1,31)
        
    codebug.set_row(2,rand)
    answer=input("What number is this in decimal notaton?\n")
    if(int(answer) == rand):
        print("You are correct!")
    else:
        print(" You got it wrong this time, the answer is " + str(rand))

#Q5 function
def logicGates(operatorAnd):
    num1=random.randint(1,31)
    num2=random.randint(1,31)
    result=num1 | num2
    
    if(operatorAnd):
        result=num1 & num2

    codebug.set_row(2,num1)
    codebug.set_row(1,num2)
    
    answer=input("What result in decimal notaton?\n")
    if(int(answer) == result):
        print("You are correct!")
    else:
        print(" You got it wrong this time, the answer is " + str(rand))
        
    codebug.set_row(4,result)

#Q1 Change the two boolean values to that you will see all numbers printed
"""
a=False
b=True

#Given Code:
if(a and b):
    codebug.write_text(0,0,"1")
elif(a):
    codebug.write_text(0,0,"2")
elif(not a and not b):
    codebug.write_text(0,0,"3")
else:
    codebug.write_text(0,0,"4")
"""

#Q2 Ask the user for their name and use "" to say "Hello name!" 
"""
name=input("What is your name?\n")
name="Hello " + name + "!"

#Code given
i=0
while(i > -5*(len(name))):
    codebug.write_text(i,0,name)
    i-=1
    time.sleep(0.25)
"""

#Q3 Make a "name length count program", which will ask the user for a sentence
#and count the length of their name(0-9)
"""
name=input("Please enter a sentence:\n")

codebug.write_text(0,0,str(len(name)))
"""


#4 Test your binary number knowledge using the CodeBug, there will be a 5bit number
#displayed on the grid and the program will ask you what the decimal equivalent is
"""
binaryToDecimal()
"""

#5 Continuing with the binary theme, we will cover binary logic, ie. AND & OR

#a)The AND Gate
"""
logicGates(True)
"""

#b)The OR Gate

logicGates(False)

