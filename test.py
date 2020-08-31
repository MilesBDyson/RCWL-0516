#!/usr/bin/env python3

from time import sleep
import motion_detector

'''
This is a basic example on how to use the HC-SR501 on the Beaglebone Black
it uses GPIO P9_12 as the trigger pin by default
to use a different pin please edit the motion_detector.py file
'''

if __name__ == "__main__":
	while True:
		if motion_detector.motion_detect():
			print("Motion Detected")
		else:
			print("Clear")
		sleep(1)
