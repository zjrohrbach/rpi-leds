import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18,GPIO.OUT)

pressed=0
while True:
	if pressed:
		if not GPIO.input(17):
			pressed=0
	else:
		if GPIO.input(17):
			pressed=1
			if GPIO.input(18):
				GPIO.output(18,0)
			else:
				GPIO.output(18,1)
	time.sleep(0.1)
