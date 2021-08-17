#!/usr/bin/env python3

from gpiozero import LED
from time import sleep

ledRed = LED(5)
ledAmber = LED(6)
ledGreen = LED(13)

def spacing():
	sleep(0.1)

def redAmberGreen():
	ledRed.on()
	spacing()
	ledRed.off()
	spacing()
	ledAmber.on()
	spacing()
	ledAmber.off()
	spacing()
	ledGreen.on()
	spacing()
	ledGreen.off()
	spacing()

while True:
	redAmberGreen()
