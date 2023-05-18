import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.IN)

GPIO.output(22, GPIO.input(23))

sleep(5)
GPIO.output(22, 0)
GPIO.cleanup() 