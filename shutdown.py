#! /usr/bin/python
import RPi.GPIO as GPIO
import os, sys, subprocess, time

# Shutdown commands needs SUDO, so is neceserly to start with sudo

buttonPin = 37 # GPIO 26, Pin 37
# The numbers printed on the board
GPIO.setmode(GPIO.BOARD)
# Use the pull up i.e. expect output to be zero. When it goes to 1, GPIO is set.
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pause = 10
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
# Clean up GPIO handler on exit of the script.
# Clean up is optional. If the system reboots it will clean up!
# GPIO.cleanup()
