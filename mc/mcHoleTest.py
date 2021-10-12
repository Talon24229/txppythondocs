from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

#Us a module to control time
import time


'''
Become a programer:

Maximize lazyness
'''


'''def snap():
        pos = mc.player.getPos()
        mc.setBlocks(pos.x + 1000, pos.y + 1000, pos.z + 1000, pos.x + -10000, pos.y + -10000, pos.z + -10000, 0)'''  

def mcDonald():
    woolGrid = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,15,15,0,0,0,0,0,0,0,0,0,0,0,0,15,15,0],
                [0,4,15,0,0,0,0,0,15,15,0,0,0,0,0,4,15,15],
                [4,4,15,0,0,0,0,4,4,15,0,0,0,0,0,4,4,15],
                [4,4,15,0,0,0,0,4,4,15,0,0,0,0,0,4,4,15],
                [4,4,15,0,0,0,0,4,4,15,0,0,0,0,0,4,4,15],
                [4,4,15,0,0,0,0,4,4,15,0,0,0,0,0,4,4,15],
                [4,4,15,0,0,0,0,4,4,15,0,0,0,0,0,4,4,15],
                [0,4,15,0,0,0,0,4,4,15,0,0,0,0,0,4,15,0],
                [0,4,4,15,0,0,4,4,4,4,15,0,0,0,4,4,15,0],
                [0,0,4,4,15,4,4,15,0,4,4,15,4,4,15,0,0,0],
                [0,0,4,4,15,4,4,15,0,4,4,15,4,4,15,0,0,0],
                [0,0,0,4,4,4,15,0,0,0,4,4,4,15,0,0,0,0],
                [0,0,0,0,4,15,0,0,0,0,0,4,15,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,15,15,15,0,0,0,15,0,0,0,0,0,0,0,0,0,0],
                [0,0,15,0,0,0,0,15,0,0,0,0,0,0,0,0,0,0],
                [0,15,15,15,0,0,15,15,15,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,15,15,15,0,0,15,0,15,0,15,0,0,0,15,0,0,0],
                [0,0,15,0,0,0,0,15,0,15,0,0,0,15,15,15,0,0],
                [0,15,15,15,0,15,0,0,0,0,0,0,15,15,15,15,15,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,15,15,0,15,15,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    pos = mc.player.getTilePos()
    for i, row in enumerate(woolGrid):
        print(row)
        for j, col in enumerate(row):
            print(col)
            mc.setBlock(pos.x + j, pos.y + i, pos.z, 35, col)


def myFunHole():
        pos = mc.player.getPos()
        mc.setBlocks(pos.x - 3, pos.y + 1000, pos.z - 3, pos.x + 5, pos.y + -10000, pos.z + 5, 0)    
    
    
def doom():
        pos = mc.player.getPos()
        mc.setBlocks(pos.x + -30, pos.y + 1000, pos.z + -30, pos.x + 20, pos.y + -10000, pos.z + 20, 0)  
    
def house():
    pos = mc.player.getPos()
    mc.setBlocks(pos.x + 1, pos.y, pos.z + 1, pos.x + 6, pos.y + 5, pos.z + 6, 1)
    mc.setBlocks(pos.x + 2, pos.y + 1, pos.z + 2, pos.x + 5, pos.y + 4, pos.z + 5, 0)
    mc.setBlocks(pos.x + 4, pos.y + 2, pos.z, pos.x + 3, pos.y + 1, pos.z + 1, 0)
    mc.setBlocks(pos.x + 2, pos.y + 4, pos.z + 2, pos.x + 5, pos.y + 4, pos.z + 2, 50)
    mc.setBlocks(pos.x + 2, pos.y + 4, pos.z + 5, pos.x + 5, pos.y + 4, pos.z + 5, 50)
    mc.setBlocks(pos.x + 2, pos.y + 3, pos.z + 2, pos.x + 2, pos.y + 3, pos.z + 2,)

#set up each pin number
GPIO.setup(6,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26,GPIO.IN, pull_up_down=GPIO.PUD_UP)

#start a loop
while True:
    
    #wait for a sec
    time.sleep(1)
    #check the first button
    if GPIO.input(6) == GPIO.LOW:
        print("Button 6 was pushed")
        mcDonald()
    elif GPIO.input(13) == GPIO.LOW:
        house()
        print("Button 13 was pushed")
    elif GPIO.input(19) == GPIO.LOW:
        print("Button 19 was pushed")
        doom()
    elif GPIO.input(26) == GPIO.LOW:
        print("Button 26 was pushed")
        while True:
            myFunHole()