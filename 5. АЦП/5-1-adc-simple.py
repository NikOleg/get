import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

def toByn(a):
    return [int (byn) for byn in bin(a)[2:].zfill(8)]

def adc():
    for i in range(256):
        GPIO.output(dac, toByn(i))
        time.sleep(0.001)
        if 1 - GPIO.input(comp):
            GPIO.output(dac, 0)
            return i

try:
    while True:
        i = adc()
        if i!= 0:
            print(i, '{:.2f}v'.format(3.3*i/256))
        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()   
