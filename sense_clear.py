#!/usr/bin/env python

from sense_hat import SenseHat
sense = SenseHat()

#script will clear LED left in on that another script may have left on

print("clearing LEDs")

sense.clear()
