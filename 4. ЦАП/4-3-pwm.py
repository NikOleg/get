import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(21, gpio.OUT)
gpio.setup(22, gpio.OUT, initial=0)
p=gpio.PWM(22, 100)
p.start(0)

try:
    while(True):
        DC=int(input())
        p.ChangeDutyCycle(DC)
        print("{:.2f}".format(DC*3.3/100))

finally:
    gpio.cleanup()