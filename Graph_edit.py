import numpy
import matplotlib.pyplot as plt
from numpy import loadtxt


with open("settings.txt", 'r') as f:

    fdata = f.readlines()

    quant = float(fdata[0])
    discr = float(fdata[1])
    expTime = float(fdata[2])

    fig, ax = plt.subplots(figsize=(16, 10), dpi=400)

    ax.grid(linewidth=1)
    ax.grid(which='minor', linestyle='--')
    ax.minorticks_on()

    ax.set_title(
        "Процесс зарядки и разрядки конденцатора в RC-цепочке", loc='center', fontsize=20)

    plt.xlabel('Время, с', fontsize=15)
    plt.xlim(0, 100)
    plt.ylabel('Напряжение, B', fontsize=15)
    plt.ylim(0, 3.5)

    plt.plot(numpy.linspace(0, expTime, int(expTime / quant)),
             [i * discr for i in loadtxt("data.txt")], 'o',  linestyle="solid", markevery=25, color='b', label="V(t)")

    plt.legend()

    plt.annotate("Время зарядки: {}, s".format(round(numpy.argmax(
        loadtxt("data.txt")) * quant)), (70, 2), fontsize=10)

    plt.annotate("Время зрзрядки: {}, s".format(round(
        expTime - numpy.argmax(loadtxt("data.txt")) * quant)), (70, 2.5), fontsize=10)

    plt.savefig("Capasitor_Graph")
