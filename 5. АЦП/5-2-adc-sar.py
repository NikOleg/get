import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 0)
GPIO.setup(comp, GPIO.IN)

def toByn(a):
    return [int (byn) for byn in bin(a)[2:].zfill(8)]

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

try:
    while True:
        k = adc()
        if k != 0:
            print(k, '{:.2f}v'.format(3.3*k/256))
        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()   