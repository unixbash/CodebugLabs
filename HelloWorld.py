import time
import RPi.GPIO as GPIO
import random

#E1
"""
username = input("Hello there, what is your name? \n")
print("Nice to meet you " + username)
"""

#E2
pin = 7
delay = 0.5

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

try:
    while True:
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(delay)
        delay = random.randint(1,90) / 100
        #print(delay)

except KeyboardInterrupt:
    print("\nKeyboard interupt.")
except:
    print("\nAn error occurred!")
finally:
    GPIO.cleanup()
