from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

#Us a module to control time
import time

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
        pos = mc.player.getTilePos()
        blockData = mc.getBlock(pos.x,pos.y - 1, pos.z)
        print(blockData)
        if blockData == 57:
            while True:
                time.sleep(5)
                mc.player.setPos(pos.x, pos.y +20, pos.z)
        
        
        #if the data block is a diomand block
        #make there postion 20 blocks higher
    elif GPIO.input(13) == GPIO.LOW:

        print("Button 13 was pushed")
    elif GPIO.input(19) == GPIO.LOW:
        print("Button 19 was pushed")

    elif GPIO.input(26) == GPIO.LOW:
        print("Button 26 was pushed")
