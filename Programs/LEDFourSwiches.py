#Talon Pauling
import RPi.GPIO as GPIO #Import Rasperry Pi GPIO library
GPIO.setWarning(False) #ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#set pin 10 to be an input pin and set inital value to be
# pulled low (off)
LEDlit = False
while True: #run forever
        if GPIO.input(6)==GPIO.HIGH:
            print("Button 1 was pushed")
            LEDlit = False
            
            
    
    










    if GPIO.input(13)==GPIO.HIGH:
        print("Button 2 was pushed")
    if GPIO.input(19)==GPIO.HIGH:
        print("Button 3 was pushed")
    if GPIO.input(26)==GPIO.HIGH:
        print("Button 4 was pushed")