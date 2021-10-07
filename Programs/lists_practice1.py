#Talon Pauling
#list practice 1
import random
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


#A var that holds more then one value is a list
groceries = ['bread','malk','eggs','cheese']
#you can get items from a list by their index
print(groceries[0])

#empty list at start
cart = []

#for every item in my list: add that to my cart
for item in groceries:
    #print("put into cart: " + item)
    cart.append(item)
print(cart)

funny = ['Dark hummer is like food, some peaple dont get it','69','420','a minute here is 60 seconds in africa','Yo moma so fat, she needed to go to sea world to get baptized','Eveyone asks who the imposter, no-one asks, how is the imposter']
number = random.randint(0,5)
print(funny[number])
#start a loop
while True:
    #wait for a sec
    time.sleep(.5)
    #check the first button
    if GPIO.input(6) == GPIO.LOW:
        print("Button 6 was pushed")
        number = random.randint(0,4)
        print(funny[number])
    elif GPIO.input(13) == GPIO.LOW:
        print("Button 13 was pushed")
    elif GPIO.input(19) == GPIO.LOW:
        print("Button 19 was pushed")
    elif GPIO.input(26) == GPIO.LOW:
        print("Button 26 was pushed")
