#!/usr/bin/env python
# displays one letter at a time
from sense_hat import SenseHat
sense = SenseHat()
import time

red = (255, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)


sense.show_letter("A", red)
time.sleep(1)
sense.show_letter("M", white)
time.sleep(1)
sense.show_letter("E", blue)
time.sleep(1)
sense.show_letter("R", red)
time.sleep(1)
sense.show_letter("I", white)
time.sleep(1)
sense.show_letter("C", blue)
time.sleep(1)
sense.show_letter("A", red)
time.sleep(1)
sense.show_letter("!", white)
time.sleep(1)
sense.clear()
