#!/usr/bin/python
import led_functions as lf
import time

red = 18
yellow = 23
green = 24
blue = 25
white = 4

lf.setup(red)
lf.setup(yellow)
lf.setup(green)
lf.setup(blue)
lf.setup(white)

lf.turn_on(red)
time.sleep(0.5)

lf.turn_off(red)
lf.turn_on(yellow)
time.sleep(0.5)

lf.turn_off(yellow)
lf.turn_on(green)
time.sleep(0.5)

lf.turn_off(green)
lf.turn_on(blue)
time.sleep(0.5)

lf.turn_off(blue)
lf.turn_on(white)
time.sleep(0.5)

lf.turn_on(red)
lf.turn_on(green)
time.sleep(0.5)

lf.turn_off(green)
lf.turn_on(yellow)
time.sleep(0.1)

lf.turn_off(yellow)
lf.turn_on(green)
time.sleep(0.1)

lf.turn_off(green)
lf.turn_on(blue)
time.sleep(0.1)

lf.turn_off(blue)
lf.turn_off(white)
lf.turn_off(red)
time.sleep(0.1)

lf.turn_on(red)
lf.turn_on(green)
lf.turn_on(white)
time.sleep(0.5)

lf.turn_off(red)
lf.turn_off(green)
lf.turn_off(white)
time.sleep(0.5)

lf.turn_on(yellow)
lf.turn_on(blue)
time.sleep(0.25)

lf.turn_off(yellow)
lf.turn_off(blue)
time.sleep(0.5)

lf.turn_on(yellow)
lf.turn_on(blue)
time.sleep(0.25)

lf.turn_off(yellow)
lf.turn_off(blue)
time.sleep(0.5)

lf.turn_on(red)
lf.turn_on(green)
lf.turn_on(white)
time.sleep(1)

lf.turn_off(red)
lf.turn_off(green)
lf.turn_off(white)
