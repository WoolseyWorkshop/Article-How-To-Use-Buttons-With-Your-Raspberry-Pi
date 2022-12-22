# button_rpigpio_basic.py
#
# Description:
# A Python program that turns on an LED when a button is pressed on a
# Raspberry Pi using the RPi.GPIO library.
#
# Circuit:
# - A momentary push button (normally open) is connected to BCM pin 5,
#   physical pin 29.
# - An LED is connected to BCM pin 21, physical pin 40.
#
# Created by John Woolsey on 10/05/2022.
# Modified by John Woolsey on 12/19/2022.
# Copyright (c) 2022 Woolsey Workshop.  All rights reserved.


# Imports
import RPi.GPIO as GPIO


# Pin Mapping
BUTTON = 5
RED_LED = 21


# Functions
def button_changed(button):
    if GPIO.input(button) == GPIO.LOW:
        print("Button pressed.")
        GPIO.output(RED_LED, GPIO.HIGH)
    else:
        print("Button released.")
        GPIO.output(RED_LED, GPIO.LOW)


# Pin Configuration
GPIO.setmode(GPIO.BCM)  # use BCM pin numbering
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # enable microcontroller's internal pull-up resistor
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.output(RED_LED, GPIO.LOW)
GPIO.add_event_detect(BUTTON, GPIO.BOTH, callback=button_changed, bouncetime=10)  # call button_changed() when button changes state with a debounce time of 10 ms


# Main
print("Press CTRL-C to exit.")
try:
    while True:
        pass
finally:  # exit cleanly when CTRL-C is pressed
    GPIO.cleanup()  # reset all GPIO resources
