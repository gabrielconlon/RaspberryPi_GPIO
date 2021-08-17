#!/usr/bin/env python3

# SAFETY FIRST
# quick little caculator for saving elevtrical components when messing around with Raspberry Pi GPIO

ohms = 0.0
amps = 0.0
volts = 0.0
watts = 0.0

volts = float(input("Enter volts: "))
ohms = float(input("Enter ohms: "))

amps = round(volts / ohms, 5)
watts = round(volts * amps, 5)


if amps < 1:
	amps = amps * 1000
	print(f"""
	ohms = {ohms}
	mili-amps = {amps} (current)
	volts = {volts}
	watts = {watts} (power)
	""")
else:
	print(f"""
	ohms = {ohms}
	amps = {amps} (current)
	volts = {volts}
	watts = {watts} (power)
	""")
