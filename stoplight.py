#!/usr/bin/env python3

from gpiozero import LED, Buzzer
from time import sleep

ledRed = LED(5)
ledAmber = LED(6)
ledGreen = LED(13)
bz = Buzzer(4)

leds = {ledRed, ledAmber, ledGreen}

slow = 5
fast = 1

def clicker():
	bz.on()
	bz.off()

def greenAmberRed():
	ledGreen.off()
	clicker()
	ledAmber.on()	
	clicker()
	sleep(programSpeed)
	ledAmber.off()
	clicker()
	ledRed.on()
	clicker()

programSpeed = int(input("Choose 'fast'(1 second intervals) or 'slow (5 second intervals): "))

repeat = 2

while repeat > 0:
	for led in leds:
		led.off()
		clicker()
	ledGreen.on()
	clicker()
	sleep(5)
	greenAmberRed()
	clicker()
	sleep(3)
	repeat -= 1
