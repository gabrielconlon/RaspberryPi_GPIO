#!/usr/bin/env python3

from gpiozero import Buzzer
from time import sleep

bz = Buzzer(4)

def trill():
	repeat = 10000
    
	while repeat > 0:
		# print(f"Seconds remaining: {repeat}")
		bz.on()
		# sleep(1)
		bz.off()
		repeat -= 1

trill()
