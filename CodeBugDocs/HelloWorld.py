import time
import RPi.GPIO as GPIO
import random

#E1
"""
username = input("Hello there, what is your name? \n")
print("Nice to meet you " + username)
"""

#E2
"""
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
"""

#E3
led = 7
pir = 11
delay = 0.1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(pir, GPIO.IN)

try:
    while True:

        if(GPIO.input(pir) == 1):
            GPIO.output(led, 1)
            
        time.sleep(delay)
        GPIO.output(led, 0)

except KeyboardInterrupt:
    print("\nKeyboard interupt.")
except:
    print("\nAn error occurred!")
finally:
    GPIO.cleanup()
