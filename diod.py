#!/usr/bin/env python
# -*- coding: utf-8 -*-
###
# Script to detect the opening of the box using a photodiode
#
import RPi.GPIO as GPIO
import os, subprocess, time

# Deff which pit will be controlled
buttonPin = 36
# The numbers printed on the board
GPIO.setmode(GPIO.BOARD)
# Use the pull up i.e. expect output to be zero. When it goes to 1, GPIO is set.
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def checkFunkc(interval):
  global buttonPin
  while True:
    if (GPIO.input(buttonPin)):
      # GPIO is 0
      # print("GPIO is 0 ")
      print("GPIO is 0")
      time.sleep(1)
    else:
      # GPIO is 1. We are here because the sensors triggered the battery being low.
      print("GPIO is 1")
      time.sleep(1)
      # Flush any stdout messages before exiting..
  

def main(args):
  # Time period to check
  interval = 10
  # Function to detect manipulation
  checkFunkc(interval)

  return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


