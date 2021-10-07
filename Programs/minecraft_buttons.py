#talon Pauling
import time
import requests
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
from mcpi.minecraft import Minecraft


GPIO.setup(6,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26,GPIO.IN, pull_up_down=GPIO.PUD_UP)
mc = Minecraft.create()



while True:
    if GPIO.input(6) == GPIO.LOW:
        requests.get("http://192.168.10.53:5000/tutd?thumb=up")
    elif GPIO.input(13) == GPIO.LOW:
        pos = mc.player.getTilePos()
        mc.postToChat(pos)
    elif GPIO.input(19) == GPIO.LOW:
        mc.player.setTilePos(0,50,0)
        #mc.player.setPos(00,00+50,00)
        
    elif GPIO.input(26) == GPIO.LOW:
        mc = Minecraft.create()
        mc.postToChat('OwO')