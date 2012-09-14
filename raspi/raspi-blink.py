#!/usr/bin/env python
import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BCM)
GREEN_LED = 18
RED_LED = 23
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

count = 0
while (count < 5):
    print "The count is: ", count
    GPIO.output(GREEN_LED, True)
    GPIO.output(RED_LED, False)
    print "Green light!"
    time.sleep(1)
    GPIO.output(GREEN_LED, False)
    GPIO.output(RED_LED, True)
    print "Red light!"
    time.sleep(1)
    count = count + 1

print "We are done now :-)"
