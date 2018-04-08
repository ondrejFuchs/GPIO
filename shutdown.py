#!/usr/bin/env python
# -*- coding: utf-8 -*-
###
# The Raspberry zero shutdown script when the battery is low
#
import RPi.GPIO as GPIO
import os, subprocess, time

# Deff which pit will be controlled
global buttonPin = 37
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
      print("Time is %s " % (time.ctime()))
      time.sleep(pause)
    else:
      # GPIO is 1. We are here because the sensors triggered the battery being low.
      print("Shutdown initiated at %s " % (time.ctime()))
      subprocess.call("shutdown -h 2 &", shell=True)
      time.sleep(2)
      # Flush any stdout messages before exiting..
      sys.stdout.flush()
      # exit the while monitoring loop.
      exit()
    # Flush any buffers if ^C or interrupt is pressed.
  sys.stdout.flush()
  

def main(args):
  # Time period to check
  interval = 10
  # Function to detect manipulation
  checkFunkc(interval)

  return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

