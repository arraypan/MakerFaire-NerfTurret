import RPi.GPIO as GPIO
from evdev import InputDevice, categorize, ecodes, KeyEvent
from select import select
import time

gamepad = InputDevice('/dev/input/event2')

servoPIN = 20
GPIO.setmode(GPIO.BCM)

GPIO.setup(servoPIN, GPIO.OUT)

GPIO.setwarnings(False)

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        keyevent = categorize(event)
        if keyevent.keystate == KeyEvent.key_down:
            print(keyevent.keycode[0])
            if keyevent.keycode[0] == 'B':
                GPIO.output(servoPIN, GPIO.LOW)
                print("set GIOP high")
                # time.sleep(2)
            else:
                GPIO.output(servoPIN, GPIO.HIGH)
        else:
                GPIO.output(servoPIN, GPIO.HIGH)


    