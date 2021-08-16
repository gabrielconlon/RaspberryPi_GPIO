#!usr/bin/env python3

from gpiozero import Buzzer
from time import sleep

bz = Buzzer(17)

def trill():
    repeat = 100000
    
    while repeat > 0:
        # print(f"Seconds remaining: {repeat * 2}")
        bz.on()
        bz.off()
        repeat -= 1

trill()
