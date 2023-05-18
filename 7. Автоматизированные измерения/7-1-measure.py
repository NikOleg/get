import RPi.GPIO as GPIO
import time
from matplotlib import pyplot

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8 ,25, 24]
comp = 4
troyka = 17

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

#снятие показаний с тройки
def adc():
    lft = 0
    rht = 255
    while (rht - lft) > 1:
        m = (rht + lft) // 2
        GPIO.output(dac, toByn(m))
        time.sleep(0.001)
        if 1 - GPIO.input(comp):
            rht = m
        else:
            lft = m
    return lft

#перевод в двоичную
def toByn(a):
    return [int (byn) for byn in bin(a)[2:].zfill(8)]

try:
    volt=0
    result_mesr=[]
    time_start=time.time()
    count=0

    #зарядка конденсатора, запис показаний в процессе
    print('начало зарядки конденсатора')
    while volt<256*0.97:
        volt=adc()
        result_mesr.append(volt)
        count+=1
        print(volt)
        GPIO.output(leds, toByn(volt))

    GPIO.setup(troyka,GPIO.OUT, initial=GPIO.LOW)

    #разрядка конденсатора, запис показаний в процессе
    print('начало разрядки конденсатора')
    while volt>256*0.02:
        volt=adc()
        result_mesr.append(volt)
        count+=1
        print(volt)
        GPIO.output(leds, toByn(volt))

    time_experiment=time.time()-time_start

    #запись данных в файлы
    print('запись данных в файл')
    with open('data.txt', 'w') as f:
        for i in result_mesr:
            f.write(str(i) + '\n')
    with open('settings.txt', 'w') as f:
        f.write(str(1/time_experiment/count) + '\n')
        f.write('0.01294')
    
    print('общая продолжительность эксперимента {}, период одного измерения {}, средняя частота дискретизации {}, шаг квантования АЦП {}'.format(time_experiment, time_experiment/count, 1/time_experiment/count, 0.013))

    #графики
    print('построение графиков')
    y=[i/256*3.3 for i in result_mesr]
    x=[i*time_experiment/count for i in range(len(result_mesr))]
    pyplot.plot(x, y)
    pyplot.xlabel('время')
    pyplot.ylabel('вольтаж')
    pyplot.show()

finally:
    GPIO.output(leds, 0)
    GPIO.output(dac, 0)
    GPIO.cleanup()