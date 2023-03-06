#Ocitaj temperaturu i ispisi 

import time
import Adafruit_DHT
import RPi.GPIO as GPIO

grejac = 18
ventilator = 23

dht11 = 4

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(grejac,GPIO.OUT)
GPIO.setup(ventilator,GPIO.OUT)

while True:
    # Remember that your sentences can only be 16 characters long!
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,dht11)
    print("temperatura: " + str(temperature))
    print("vlaznost: " + humidity)
    time.sleep(2)


