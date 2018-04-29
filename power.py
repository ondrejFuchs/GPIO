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
# Threshold of positive check
threshold = 60
# The numbers printed on the board
GPIO.setmode(GPIO.BOARD)
# Use the pull up i.e. expect output to be zero. When it goes to 1, GPIO is set.
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def checkFunkc():
  global buttonPin
  global interval
  global threshold
  stateOld = 0
  stateNow = 0
  counter = 0
  while True:
    stateOld = stateNow 
    if (GPIO.input(buttonPin)):
      # GPIO is 0
      counter = 0
      stateNow = 0
      if stateNow != stateOld:
        logging.debug('Changing the power to adapter')
        print("Power by adapter")
      time.sleep(interval)
    else:
      # GPIO is 1
      counter += 1
      stateNow = 1
      if stateNow != stateOld:
        logging.debug('Changing the power to battery')
        print("Power by battery")
      # After 60 sec shutdown  
      if counter > threshold:
        #TODO: Vypnout nahrávání !!!
        subprocess.call("shutdown -h now &", shell=True)
        counter = 0  
        # Flush any stdout messages before exiting..
        sys.stdout.flush()
        # exit the while monitoring loop.
        exit()
      #logging.debug('This message should go to the log file')
      time.sleep(interval)
     
  
def main(args):
  # Remove or make log file 
  if not os.path.exists('/var/log/power.log'):
    os.mknod('/var/log/power.log')
  else:
    os.remove('/var/log/power.log')
    os.mknod('/var/log/power.log')  
  # Set format for loggin
  logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y-%m-%d_%H-%M-%S',filename='/var/log/power.log',level=logging.DEBUG)  
  # Function to detect manipulation
  checkFunkc()

  return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


