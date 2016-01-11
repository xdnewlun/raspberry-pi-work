import RPi.GPIO as gpio
import time
import random

from enemy import chooseEnemy


gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

gpio.setup(17,gpio.IN) #Right Button
gpio.setup(27,gpio.IN) #Left Button

gpio.setup(13,gpio.OUT) #User RED LED
gpio.setup(6, gpio.OUT) #User YELLOW LED
gpio.setup(5,gpio.OUT) #User Green LED

gpio.setup(23,gpio.OUT) #Enemy RED LED
gpio.setup(24, gpio.OUT) #Enemy YELLOW LED
gpio.setup(25,gpio.OUT) #Enemy Green LED

for i in range(0, 100):
    print ""

def start():
    print("Please press the 'Action Button' To Start!")
    #while True:
    if gpio.input(27) == False:
        chooseEnemy()
start()
