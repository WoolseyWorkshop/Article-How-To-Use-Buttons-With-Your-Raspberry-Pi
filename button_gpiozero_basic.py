# button_gpiozero_basic.py
#
# Description:
# A Python program that turns on an LED when a button is pressed on a
# Raspberry Pi using the GPIO Zero library.
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


# Functions
def button_pressed():
    print("Button pressed.")
    red_led.on()

def button_released():
    print("Button released.")
    red_led.off()


# Main
red_led.off()
button.when_pressed = button_pressed  # call button_pressed() when button is pressed
button.when_released = button_released  # call button_released() when button is released
print("Press CTRL-C to exit.")
pause()
