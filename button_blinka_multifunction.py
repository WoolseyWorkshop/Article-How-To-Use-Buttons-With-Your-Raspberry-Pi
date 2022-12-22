# button_blinka_multifunction.py
#
# Description:
# A Python program that toggles the blink rate of an LED when a button is
# pressed on a Raspberry Pi using the Blinka (CircuitPython) library.
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
from time import monotonic
import board
from digitalio import DigitalInOut, Direction, Pull
from adafruit_debouncer import Debouncer
import RPi.GPIO as GPIO


# Pin Mapping
button_pin = DigitalInOut(board.D5)
red_led = DigitalInOut(board.D21)


# Global Variables
quick_blink = False
previous_blink_time = 0


# Pin Configuration
button_pin.direction = Direction.INPUT
button_pin.pull = Pull.UP  # enable microcontroller's internal pull-up resistor
button = Debouncer(button_pin)  # enable button debouncing
red_led.direction = Direction.OUTPUT
red_led.value = False


# Main
print("Press CTRL-C to exit.")
try:
    while True:
        button.update()  # read and update button state
        if button.fell:
            print("Button pressed.")
            quick_blink = not quick_blink  # toggle blink rate
        current_time = monotonic()
        delay = 0.5 if quick_blink else 1
        if current_time - previous_blink_time >= delay:  # delay for appropriate time
            red_led.value = not red_led.value  # toggle LED state
            previous_blink_time = current_time
finally:  # exit cleanly when CTRL-C is pressed
    GPIO.cleanup()  # reset all GPIO resources
