import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def setup(color):
	GPIO.setup(color,GPIO.OUT)

def turn_on(color):
	GPIO.output(color,GPIO.HIGH)
	print "LED On"

def turn_off(color):
	GPIO.output(color,GPIO.LOW)
	print "LED Off"

def flash(color):
	turn_on(color)
	time.sleep(1)
	turn_off(color)
