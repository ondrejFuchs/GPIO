#!/usr/bin/env python
# -*- coding: utf-8 -*-
###
# Script to detect change power from adapter to battery
#
import RPi.GPIO as GPIO
import os, subprocess, time, logging

# Deff which pit will be controlled
buttonPin = 36
# Interval to check
interval = 1
# The numbers printed on the board
GPIO.setmode(GPIO.BOARD)
# Use the pull up i.e. expect output to be zero. When it goes to 1, GPIO is set.
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# Set format for loggin
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y-%m-%d_%H-%M-%S',filename='/var/log/power.log',level=logging.DEBUG)

def checkFunkc():
  global buttonPin
  global interval
  stateOld = 0
  stateNow = 0
  while True:
    stateOld = stateNow 
    if (GPIO.input(buttonPin)):
      # GPIO is 0
      stateNow = 0
      if stateNow != stateOld:
        logging.debug('Changing the power to adapter')
        print("GPIO is 0")
      time.sleep(interval)
    else:
      # GPIO is 1
      stateNow = 1
      if stateNow != stateOld:
        logging.debug('Changing the power to battery')
        print("GPIO is 1")
      #logging.debug('This message should go to the log file')
      time.sleep(interval)
     
  
def main(args):
  # Make log file
  if not os.path.exists('/var/log/power.log'):
    os.mknod('/var/log/power.log')
  # Function to detect manipulation
  checkFunkc()

  return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


