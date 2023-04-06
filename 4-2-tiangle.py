import RPi.GPIO as GPIO
import time as t

GPIO.setmode(GPIO.BCM)


dac = [26, 19, 13, 6, 5, 11, 9, 10]


GPIO.setup(dac, GPIO.OUT)

def decTObin(a):
    return[int(bit) for bit in format(a, 'b').zfill(8)]

print("Введите период в секундах")
tm = int(input())

T = tm / 256 / 2

try:
    while True:
        for a in range (255):
            GPIO.output(dac, decTObin(a))
            t.sleep(T)
        for a in range (255):
            GPIO.output(dac, decTObin(255 - a))
            t.sleep(T)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

