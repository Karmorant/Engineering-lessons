import RPi.GPIO as GPIO
import time as t
import matplotlib.pyplot as plt
from numpy import loadtxt

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

troyka_data = []

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
    S_CH_time = t.time()
    val = 0
    #зарядка
    while val < 230:
        arr = [i for i in range(256)]
        val = adc(arr)
        troyka_data.append(val)


        voltage = val / 256 * 3.3

        print("Цифровое значение: ", val)
        print("Значение напряжения: ", voltage)

        b = int(val / 256 * 10)
        ledarr = [0]*8

        for i in range (b - 1):
            ledarr[i] = 1

        GPIO.output(leds, ledarr)
        t.sleep(0.1)



    GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
    
    while val > 64:
        val = adc(arr)
        troyka_data.append(val)
        
    EXP_time = t.time() - S_CH_time



    with open("data.txt", 'w') as f:
        print(*troyka_data, sep='\n', end='\n', file=f)

    with open("settings.txt", 'w') as f:
        f.write(str(EXP_time / len(troyka_data)))
        f.write("\n")   
        f.write(str(3.3/256))
        f.write("\n")
        f.write(str(EXP_time))



    import numpy
    with open("settings.txt", 'r') as f:

        fdata = f.readlines()

        quant = float(fdata[0])
        discr = float(fdata[1])
        expTime = float(fdata[2])

        
        plt.plot(numpy.linspace(0, expTime, int(expTime / quant)), [i * discr for i in loadtxt("data.txt")])
        plt.show()
        print ("Время эксперемента:", expTime)
finally:
    
    GPIO.output(dac, 0)
    GPIO.cleanup()



                
