"""
    ***In all labs, students are expected to use Scratch code creator/emulator
    on CodeBug's website in order to understand the logic of the program, before they run it.

    In this lab students will learn variables and variable types
"""
import time
import codebug_i2c_tether
import codebug_tether.sprites

codebug=codebug_i2c_tether.CodeBug()
codebug.open()
codebug.clear()

#Q1 Create a variable called favNum and make it equal to your
#favourite digit, afterwards use codebug.write_text(0,0,str(favNum))

favNum=5
codebug.write_text(0,0,str(favNum))

#Q2 Write create a variable name and set it equal to the first character
#of your name. Print it on the CodeBug using codebug.write_text(0,0,name)
codebug.clear()

name='F'
write_text(0,0,name)

#Q3 Using a function codebug.set_pixel(X,Y,1), turn on the middle pixel on the CodeBug 

codebug.clear()

codebug.set_pixel(2,2,1)


#4 Using the function codebug.set_row(Y,0b11111) draw:
#a) Smiley face b) Sad face c) Laughing face d) Heart shape
codebug.clear()

#a)Smiley face
codebug.set_row(4,0b01010)
codebug.set_row(3,0b01010)
codebug.set_row(2,0b00000)
codebug.set_row(1,0b10001)
codebug.set_row(0,0b01110)

#d)Heart shape
codebug.clear()
codebug.set_row(4,0b01010)
codebug.set_row(3,0b11111)
codebug.set_row(2,0b11111)
codebug.set_row(1,0b01110)
codebug.set_row(0,0b00100)

