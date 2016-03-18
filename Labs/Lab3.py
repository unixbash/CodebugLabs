"""
    ***In all labs, students are expected to use Scratch code creator/emulator
    on CodeBug's website in order to understand the logic of the program, before they run it.

    In this lab students will learn loops, while and for
"""
import time
import codebug_i2c_tether

codebug=codebug_i2c_tether.CodeBug()
codebug.open()

#Q1 Create a variable called favNum and make it equal to your
#favourite digit, afterwards use codebug.write_text(0,0,str(favNum))

favNum=5
codebug.write_text(0,0,str(favNum))

#Q2


"""
import codebug_i2c_tether
import time

codebug=codebug_i2c_tether.CodeBug()
codebug.open()

#Q1 Create a program that will count from 0 to 9 on the CodeBug
num=0
while(num < 10):
    codebug.clear()
    codebug.write_text(0,0,str(num))
    num += 1
    time.sleep(1)
"""
