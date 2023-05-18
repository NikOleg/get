import RPi.GPIO as gpio
import time

dac=[26, 19, 13, 6, 5, 11, 9, 10]
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

def toBinary(a, n):
    return [int (elem) for elem in bin(a) [2:].zfill(n)]

try:
    T = input('Enter a period\n')
    while(True):
        if T=='q':
            sys.exit()
        if not T.isdigit():
            print('Please, enter a number')
            continue
        t = int(T)/512
        for i in range(256):
            gpio.output(dac, toBinary(i, 8))
            time.sleep(t)
        for i in range(255, -1, -1):
            gpio.output(dac, toBinary(i, 8))
            time.sleep(t)   
         
finally:
    gpio.output(dac, 0)
    gpio.cleanup()