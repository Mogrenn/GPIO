import RPi.GPIO as GPIO
import time


def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)


def forward(tf):
    init()
    GPIO.output(17, True)
    GPIO.output(27, False)
    time.sleep(tf)
    GPIO.cleanup()


def reverse(tf):
    init()
    GPIO.output(17, False)
    GPIO.output(27, True)
    time.sleep(tf)
    GPIO.cleanup()


forward(4)
reverse(2)
