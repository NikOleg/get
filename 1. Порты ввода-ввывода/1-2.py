import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT)

for i in range(16):
    GPIO.output(14, 1)
    sleep(0.5)
    GPIO.output(14, 0)
    sleep(0.5)

GPIO.reset()