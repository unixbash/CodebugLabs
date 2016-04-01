"""
    ***In all labs, students are expected to use Scratch code creator/emulator
    on CodeBug's website in order to understand the logic of the program, before they run it.

    In this lab students will learn flow controll, mainly if statements
"""

import time
import codebug_i2c_tether

codebug=codebug_i2c_tether.CodeBug()
codebug.open()
codebug.clear()

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

#Q3 

