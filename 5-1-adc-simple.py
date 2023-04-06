import RPi.GPIO as GPIO
import time as t

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(comp, GPIO.IN)


def decTObin(a):
    return[int(bit) for bit in format(a, 'b').zfill(8)]

def adc():
    
    for value in range(256):
        GPIO.output(dac, decTObin(value))
        t.sleep(0.001)
        compV = GPIO.input(comp)
        if compV == 0 :
            return value
            break

try:
    while True:
        voltage = adc() / 256 * 3.3
        print("Цифровое значение: ", adc())
        print("Значение напряжения: ", voltage)
         
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

                
