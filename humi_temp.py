#!/usr/bin/python3

import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11

pin = 2

while(1):
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

	if humidity is not None and temperature is not None:
		print ('Temp={0:0.4f}*C Humidity={1:0.4f}%'.format(temperature, humidity))
	else:
		print ('Failed to get reading. Try again!')
