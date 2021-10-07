import requests
import time

while True:
    x = requests.get('http://192.168.10.53:5000/sfx#:~:text=nogodpleaseno-,ohyesdaddy,-peanutbutterjelly')
    print(x.status_code)
    time.sleep(1)
    