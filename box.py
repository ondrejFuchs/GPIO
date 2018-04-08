#!/usr/bin/env python
# -*- coding: utf-8 -*-
###
# Script to detect tampering with the box
#
import RPi.GPIO as GPIO
import os, subprocess, time

# The numbers printed on the board
GPIO.setmode(GPIO.BOARD)
# Use the pull up i.e. expect output to be zero. When it goes to 1, GPIO is set.
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def checkFunkc(interval, buttonPin):
  print "TODO"
  

def main(args):
  # Deff which pit will be controlled
  buttonPin = 37
  # Time period to check
  interval = 10
  # Function to detect manipulation
  checkFunkc(interval, buttonPin)

  return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

