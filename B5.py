#Ocitaj temperaturu, ako je temperatura vece od 25 ukljuci ventilator
#ako je temperatura manje od 25 ukljuci grejac
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
humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,17)

givenTemp = 25.0



while True:
    # Remember that your sentences can only be 16 characters long!
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,17)
    time.sleep(2)
    
    print("temperatura: " + str(temperature))
    print("vlaznost: " + humidity)

    if temperature > givenTemp:
        GPIO.output(ventilator, GPIO.HIGH)
        GPIO.output(grejac, GPIO.LOW)
    
    if temperature < givenTemp:
        GPIO.output(ventilator, GPIO.LOW)
        GPIO.output(grejac, GPIO.HIGH)
    
    time.sleep(2)


