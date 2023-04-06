import RPi.GPIO as GPIO
import time as t

GPIO.setmode(GPIO.BCM)

leds = [21, 20, 16, 12, 7, 8, 25,24]


GPIO.setup(leds, GPIO.OUT)

for i in range (4):
    for led in leds:
        GPIO.output(led, 1)
        t.sleep (0.2)
        GPIO.output(leds, 0)

GPIO.cleanup()