'''Talon Pauling
Places a random colored wool block'''

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

#Us a module to control time
import time



counter = 0

#35, 1 2 3 4 5
woolColors = [6, 5, 10]

def placeNext(direction):
    global counter
    counter += direction
    if counter < 0:
        counter = 2
    if counter > 2:
        counter = 0
    mc.setBlock(-4,13,-64,35,woolColors[counter])

        
while True:
    
        #set up each pin number
    GPIO.setup(6,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(13,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    

    #start a loop
    while True:
        
        #wait for a sec
        time.sleep(1)
        #check the first button
        if GPIO.input(6) == GPIO.LOW:
            print("Button 6 was pushed")
            placeNext(1)
        elif GPIO.input(13) == GPIO.LOW:
            print("Button 13 was pushed")
            placeNext(-1)

'''
Set up a program for MC and two buttons *
Create a 'counter' variable that starts at 0 *
create a list of blockdata numbers for different color wool *
define a funtion called placeNext *
    -it takes one argument called direction *
    -it changes the counter by adding the direction argument *
    -place a wool block of color from the list where
     the index matches the counter variable *
    -If the counter is out of bounds of the index, reset it *
In a forever loop:
    -if the first button was pressed, placeNext (1)
    -if the first button was pressed, placeNext (-1)
'''















