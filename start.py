import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT) #ENABLE MOTOR PIN
GPIO.setup(27, GPIO.OUT) #IN1 FOR MOTOR 1

while True:
    GPIO.output(17, GPIO.HIGH)
    #GPIO.output(27, GPIO.HIGH)
