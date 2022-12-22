// button_pigpio_multifunction.c
//
// Description:
// A C program that toggles the blink rate of an LED when a button is
// pressed on a Raspberry Pi using the pigpio library.
//
// Circuit:
// - A momentary push button (normally open) is connected to BCM pin 5,
//   physical pin 29.
// - An LED is connected to BCM pin 21, physical pin 40.
//
// Created by John Woolsey on 10/07/2022.
// Modified by John Woolsey on 12/19/2022.
// Copyright (c) 2022 Woolsey Workshop.  All rights reserved.


// Includes
#include <signal.h>
#include <stdio.h>
#include <pigpio.h>


// Pin Mapping
const int Button = 5;
const int RedLED = 21;


// Global Variables
volatile sig_atomic_t signal_received = 0;  // interrupt signal received
int quick_blink = 0;


// Functions
void sigint_handler(int signal) {
   signal_received = signal;  // capture interrupt signal
}

void buttonChanged(int gpio, int level, uint32_t tick) {
   static uint32_t previousTimeButtonChanged = 0;
   uint32_t currentTime = tick;
   if (currentTime - previousTimeButtonChanged > 10000) {  // debounce time of 10 ms
      if (level == PI_LOW) {
         printf("Button pressed.\n");
         quick_blink = (quick_blink) ? 0 : 1;  // toggle blink rate
      } else if (level == PI_TIMEOUT) {
         printf("Timeout occurred.\n");
      }
      previousTimeButtonChanged = currentTime;
   }
}


// Main
int main() {
   // Initialize pigpio library GPIO interface
   if (gpioInitialise() == PI_INIT_FAILED) {
      printf("ERROR: Failed to initialize the GPIO interface.\n");
      return 1;  // exit with positive number to denote failure
   }

   // Pin configuration
   gpioSetMode(Button, PI_INPUT);
   gpioSetPullUpDown(Button, PI_PUD_UP);  // enable microcontroller's internal pull-up resistor
   gpioSetMode(RedLED, PI_OUTPUT);
   gpioWrite(RedLED, PI_LOW);
   gpioSetAlertFunc(Button, buttonChanged);  // call buttonChanged() when button changes state

   // Detect when CTRL-C is pressed
   signal(SIGINT, sigint_handler);  // enable interrupt handler
   printf("Press CTRL-C to exit.\n");
   while (!signal_received) {  // loops until CTRL-C is pressed
      gpioWrite(RedLED, !gpioRead(RedLED));  // toggle LED state
      (quick_blink) ? time_sleep(0.5) : time_sleep(1);  // sleep for appropriate time
   }

   // Exit cleanly when CTRL-C is pressed
   gpioSetMode(RedLED, PI_INPUT);  // reset RedLED pin as an input
   gpioTerminate();  // terminate pigpio library GPIO interface
   printf("\n");
   return 0;  // exit with zero to denote success
}
