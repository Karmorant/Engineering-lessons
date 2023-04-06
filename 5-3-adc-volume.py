import RPi.GPIO as GPIO
import time as t

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(comp, GPIO.IN)


def decTObin(decNum):
    return[int(bit) for bit in '{0:b}'.format(decNum).zfill(8)]





def adc(arr: list):
    if len(arr) == 1:
        return arr[0]
    
    GPIO.output(dac, decTObin(arr[len(arr)//2]))
    t.sleep(0.01)
    compV = GPIO.input(comp)

    if compV == GPIO.LOW :
        return adc(arr[:len(arr)//2])
    else:
        return adc(arr[len(arr)//2:])



try:
    while True:
        arr = [i for i in range(256)]
        a = adc(arr)
        voltage = a / 256 * 3.3
        print("Цифровое значение: ", a)
        print("Значение напряжения: ", voltage)
        b = int(a / 256 * 10)
        ledarr = [0]*8
        for i in range (b - 1):
            ledarr[i] = 1
        GPIO.output(leds, ledarr)
        t.sleep(0.1)
         
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

                
