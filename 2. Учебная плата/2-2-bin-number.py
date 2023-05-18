import RPi.GPIO as GPIO
import time

dac    = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0, 0, 0, 0, 0, 0, 0, 0]

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

if len(dac) == len(number):
    for i in range(len(dac)):
        GPIO.output(dac[i], number[i])

time.sleep(12)
GPIO.output(dac, 0)
GPIO.cleanup()

'''2 - 0,48
    255 - 3,26
    127 - 1,62
    64 - 0,82
    32 - 0,5
    5 - 0,48
    0 - 0,48
'''