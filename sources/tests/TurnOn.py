import RPi.GPIO as GPIO
import time

# Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

# Turn On
GPIO.output(7, True)

# Leave on for 5 seconds
time.sleep(5)

# Turn off
GPIO.output(7, False)

# Will Reset the GPIO
GPIO.cleanup()
