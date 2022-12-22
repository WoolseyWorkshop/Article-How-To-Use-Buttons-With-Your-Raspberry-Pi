# button_gpiozero_multifunction.py
#
# Description:
# A Python program that toggles the blink rate of an LED when a button is
# pressed on a Raspberry Pi using the GPIO Zero library.
#
# Circuit:
# - A momentary push button (normally open) is connected to BCM pin 5,
#   physical pin 29.
# - An LED is connected to BCM pin 21, physical pin 40.
#
# Created by John Woolsey on 10/05/2022.
# Modified by John Woolsey on 12/07/2022.
# Copyright (c) 2022 Woolsey Workshop.  All rights reserved.


# Imports
from signal import pause
from gpiozero import Button, LED


# Pin Mapping
button = Button(5)
red_led = LED(21)


# Global Variables
quick_blink = False


# Functions
def button_pressed():
    global quick_blink
    print("Button pressed.")
    quick_blink = not quick_blink  # toggle blink rate
    red_led.blink(on_time=0.5, off_time=0.5) if quick_blink else red_led.blink()  # sleep for appropriate time


# Main
red_led.off()
button.when_pressed = button_pressed  # call button_pressed() when button is pressed
print("Press CTRL-C to exit.")
red_led.blink()
pause()
