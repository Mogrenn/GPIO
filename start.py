import RPi.GPIO as GPIO
from pynput.keyboard import Key, Listener

import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT) #IN1 FOR MOTOR 1
GPIO.setup(27, GPIO.OUT) #IN2 FOR MOTOR 2

def on_press(key):
    print('{0} pressed'.format(
        key))
    try:
        if key.char == 'w':
            print("hje")
            # GPIO.output(17, GPIO.HIGH)
        elif key.char == "s":
            # GPIO.output(27, GPIO.HIGH)
    except Exception as e:
        print(e)


def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False
    elif key.char == 'w':
        GPIO.output(17, GPIO.HIGH)
    elif key.char == "s":
        GPIO.output(27, GPIO.HIGH)


# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

#GPIO.output(17, GPIO.HIGH)
#GPIO.output(27, GPIO.HIGH)

#GPIO.output(17, GPIO.LOW)
#GPIO.output(27, GPIO.LOW)
#GPIO.output(17, True)
#GPIO.output(27, True)
