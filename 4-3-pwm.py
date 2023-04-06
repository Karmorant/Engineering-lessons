import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

p = GPIO.PWM(22, 50)
p2 = GPIO.PWM(21, 50)
try:
    while True:
        print("Введите коэффицент")
        a = int(input())
        p.start(a)
        p2.start(a)
        print("Расчётное напряжение:", int(a) * 3.3 / 100)
            
finally:
    GPIO.output(22, 0)
    GPIO.output(21, 0)
    GPIO.cleanup()

