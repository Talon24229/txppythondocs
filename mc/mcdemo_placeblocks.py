#Talon P replace block under you
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering


#Us a module for requesting data online
import requests

#Us a module to control time
import time


'''
Become a programer:

Maximize lazyness
'''





def clearBlock():
        pos = mc.player.getPos()
        mc.setBlocks(pos.x + 1, pos.y, pos.z + 1, pos.x + 6, pos.y + 5, pos.z + 6, 0)

def house():
    pos = mc.player.getPos()
    mc.setBlocks(pos.x + 1, pos.y, pos.z + 1, pos.x + 6, pos.y + 5, pos.z + 6, 1)
    mc.setBlocks(pos.x + 2, pos.y + 1, pos.z + 2, pos.x + 5, pos.y + 4, pos.z + 5, 0)
    mc.setBlocks(pos.x + 4, pos.y + 2, pos.z, pos.x + 3, pos.y + 1, pos.z + 1, 0)
    mc.setBlocks(pos.x + 2, pos.y + 4, pos.z + 2, pos.x + 5, pos.y + 4, pos.z + 2, 50)
    mc.setBlocks(pos.x + 2, pos.y + 4, pos.z + 5, pos.x + 5, pos.y + 4, pos.z + 5, 50)
    mc.setBlocks(pos.x + 2, pos.y + 3, pos.z + 2, pos.x + 2, pos.y + 3, pos.z + 2, 37)

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
        house()
        requests.get("http://192.168.10.53:5000/sfx?file=nogodpleaseno")
    elif GPIO.input(13) == GPIO.LOW:
        clearBlock()
        print("Button 13 was pushed")
    elif GPIO.input(19) == GPIO.LOW:
        print("Button 19 was pushed")
    elif GPIO.input(26) == GPIO.LOW:
        print("Button 26 was pushed")

