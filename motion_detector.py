#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
from time import sleep
import datetime

'''
This file has been modified for the Beaglebone Black
it uses P9_12 as the trigger pin by default
it uses P9_30 as the enable/disable pin by default
run this file directly as a standalone or import it
into your project as needed
'''

trigger_pin = "P9_12"
enable_pin = "P9_30"

GPIO.setup(trigger_pin, GPIO.IN)
GPIO.setup(enable_pin, GPIO.OUT)

GPIO.output(enable_pin, GPIO.HIGH)  # Enable Sensor
#GPIO.output(enable_pin, GPIO.LOW)    # Disable Sensor


def detect():
	while True:
		if GPIO.input(trigger_pin) == True:
			print(str(datetime.datetime.now()) + "    Motion Detected.")
		else:
			print(str(datetime.datetime.now()) + "    All Clear.")
		sleep(1)


def motion_detect():
	motion = GPIO.input(trigger_pin)
	GPIO.cleanup()
	return motion

if __name__ == "__main__":
	detect()
	GPIO.cleanup()
