"""
    ***In all labs, students are expected to use Scratch code creator/emulator
    on CodeBug's website in order to understand the logic of the program, before they run it.

    In this lab students will learn flow controll, mainly if statements
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
