import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT) #ENABLE MOTOR PIN
GPIO.setup(27, GPIO.OUT) #IN1 FOR MOTOR 1
GPIO.setup(22, GPIO.OUT) #IN2 FOR MOTOR 2

#GPIO.output(17, GPIO.HIGH)
#GPIO.output(27, GPIO.HIGH)

#GPIO.output(17, GPIO.LOW)
#GPIO.output(27, GPIO.LOW)
GPIO.output(17, True)
GPIO.output(27, True)
GPIO.output(22, True)
