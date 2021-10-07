#Talon Pauling
#four buttons one led

#setup for button and led
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering


#Us a module for requesting data online
import requests

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
        requests.get("http://192.168.10.53:5000/sfx?file=nogodpleaseno")
    elif GPIO.input(13) == GPIO.LOW:
        print("Button 13 was pushed")
    elif GPIO.input(19) == GPIO.LOW:
        print("Button 19 was pushed")
    elif GPIO.input(26) == GPIO.LOW:
        print("Button 26 was pushed")