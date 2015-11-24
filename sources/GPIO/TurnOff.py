import RPi.GPIO as GPIO
import sys

# Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(int(sys.argv[1]), GPIO.OUT)

# Turn On
#GPIO.output(sys.argv[1], True)

# Turn off
GPIO.output(int(sys.argv[1]), False)

# Will Reset the GPIO
GPIO.cleanup()
