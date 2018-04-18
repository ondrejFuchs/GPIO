#!/usr/bin/env python
# -*- coding: utf-8 -*-
###
# Script to detect the opening of the box using a photodiode
#
import RPi.GPIO as GPIO
import os, subprocess, time, logging

# Deff which pit will be controlled
buttonPin = 36
# Interval to check
interval = 1
# Threshold of positive check
threshold = 5
# The numbers printed on the board
GPIO.setmode(GPIO.BOARD)
# Use the pull up i.e. expect output to be zero. When it goes to 1, GPIO is set.
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Set format for loggin
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y-%m-%d_%H-%M-%S',filename='/var/log/power.log',level=logging.DEBUG)

def checkFunkc():
  global buttonPin
  global interval
  global threshold
  counter = 0
  while True:
    if (GPIO.input(buttonPin)):
      # GPIO is 0
      counter = 0
      print("Box is closed")
      time.sleep(interval)
    else:
      # GPIO is 1
      counter += 1
      print("Box is open")
      if counter > threshold:
          logging.debug('Box is open')
          print("ALARM")
          counter = 0
      #logging.debug('This message should go to the log file')
      time.sleep(interval)
  

def main(args):
  # Make log file
  if not os.path.exists('/var/log/diod.log'):
    os.mknod('/var/log/diod.log')
  # Function to detect manipulation
  checkFunkc()

  return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


