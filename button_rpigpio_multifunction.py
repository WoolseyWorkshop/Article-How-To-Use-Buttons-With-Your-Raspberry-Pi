# button_rpigpio_multifunction.py
#
# Description:
# A Python program that toggles the blink rate of an LED when a button is
# pressed on a Raspberry Pi using the RPi.GPIO library.
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
from time import sleep
import RPi.GPIO as GPIO


# Pin Mapping
BUTTON = 5
RED_LED = 21


# Global Variables
quick_blink = False


# Functions
def button_pressed(button):
    global quick_blink
    print("Button pressed.")
    quick_blink = not quick_blink  # toggle blink rate


# Pin Configuration
GPIO.setmode(GPIO.BCM)  # use BCM pin numbering
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # enable microcontroller's internal pull-up resistor
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.output(RED_LED, GPIO.LOW)
GPIO.add_event_detect(BUTTON, GPIO.FALLING, callback=button_pressed, bouncetime=10)  # call button_pressed() when button changes state with a debounce time of 10 ms


# Main
print("Press CTRL-C to exit.")
try:
    while True:
        GPIO.output(RED_LED, not GPIO.input(RED_LED))  # toggle LED state
        sleep(0.5) if quick_blink else sleep(1)  # sleep for appropriate time
finally:  # exit cleanly when CTRL-C is pressed
    GPIO.cleanup()  # reset all GPIO resources
