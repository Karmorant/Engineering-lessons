import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)


dac = [26, 19, 13, 6, 5, 11, 9, 10]


GPIO.setup(dac, GPIO.OUT)

def decTObin(a):
    return[int(bit) for bit in format(a, 'b').zfill(8)]

try:
    while True:
        a = input()
        
        if a=='q':
            raise KeyboardInterrupt()

        elif a.isnumeric() and int(a) <= 255:
            GPIO.output(dac, decTObin(round(float(a))))
            print("Ожидаемое напряжение на ЦАП:",float(a)/256* 3.3)

        else:
            print("Число не входит в ожидаемый диапазон")
        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
