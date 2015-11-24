import RPi.GPIO as GPIO
import time

def GPIO_On_Off(pinNumber):

	# Setup
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pinNumber, GPIO.OUT)

	# Turn On
	GPIO.output(pinNumber, True)

	# Leave on for 5 seconds
	time.sleep(0.1)

	# Turn off
	GPIO.output(pinNumber, False)

	# Will Reset the GPIO
	GPIO.cleanup()

while True:
	GPIO_On_Off(35)
	GPIO_On_Off(36)
	GPIO_On_Off(37)
	GPIO_On_Off(38)
