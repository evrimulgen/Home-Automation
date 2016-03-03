import RPi.GPIO as GPIO
import sys
import time

# Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

# Turn On
GPIO.output(12, True)

# Sleep
time.sleep(10)

# Turn off
GPIO.output(12, False)

# Will Reset the GPIO
GPIO.cleanup()
