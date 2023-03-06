#napravi program "baci kocku"
#kad pritisnes taster treba da generise broj od 1 do 6 i da ispise
#treba da brojimo broj pritisaka i da ispisemo

import time
import random
import RPi.GPIO as GPIO

buttonPin = 17

click = 0

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buttonPin,GPIO.IN)

def button_callback(buttonPin ):
    global click
    click += 1
    number = random.randint(1,6)
    print("vas " + str(click)+"i " + " broj je " + str(number))  
    
    if number == 6:
        print("ponovi bacanje")


GPIO.add_event_detect(buttonPin, GPIO.RISING, callback = button_callback, bouncetime = 800)


while True:
    time.sleep(0.01)
