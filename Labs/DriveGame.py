import codebug_i2c_tether
import time
from random import randint

codebug=codebug_i2c_tether.CodeBug()
codebug.open()

class DriveGame:
    'This is the DriveGame Class'

    gamecountdown=3           
    position=[4,4]
    passenger=[randint(0,3),randint(0,3)]

    def __init__(self):

        self.gamestart()

        codebug.set_pixel(self.position[0], self.position[1], 1)
        codebug.set_pixel(self.passenger[0], self.passenger[1], 1)

    def gamestart(self):
        codebug.clear()
        codebug.write_text(0,0,'The game starts in')
        while(self.gamecountdown > 0):
            codebug.clear()
            codebug.write_text(0,0,str(self.gamecountdown))
            self.gamecountdown -= 1
            time.sleep(1)
        codebug.clear()

    def moveTemplate(self, pos, limit, greater, increment):
        if(greater):
            if(self.position[pos] > limit):
                codebug.set_pixel(self.position[0], self.position[1], 0) 
                if(increment):
                    self.position[pos] += 1
                else:
                    self.position[pos] -= 1
        else:
            if(self.position[pos] < limit):
                codebug.set_pixel(self.position[0], self.position[1], 0) 
                if(increment):
                    self.position[pos] += 1
                else:
                    self.position[pos] -= 1
                
        codebug.set_pixel(self.position[0], self.position[1], 1)
        
        
    def moveLeft(self):
        self.moveTemplate(0,4,False,True)

    def moveRight(self):
        self.moveTemplate(0,0,True,False)
    
    def moveUp(self):
        self.moveTemplate(1,0,True,False)

    def moveDown(self):
        self.moveTemplate(1,4,False,True)

drive=DriveGame()

while(True):
    if(codebug.get_input("A")==1):
        drive.moveRight()
    if(codebug.get_input("B")==1):
        drive.moveLeft()
    if(codebug.get_input(0)== 0):
        drive.moveDown()
    if(codebug.get_input(2)== 0):
        drive.moveUp()
    time.sleep(.2)
