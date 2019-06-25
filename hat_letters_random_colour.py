#!/usr/bin/env python
#script displays letters with random colors
from sense_hat import SenseHat
import time
import random
sense = SenseHat()
#assign a random numbaer between 0-255 to a variable r
r = random.randint(0, 255)
print("the random number is"), r, ("this time")

sense.show_letter("H", (r, 0, 0))
time.sleep(1)
sense.show_letter("i", (0, r, 0))
time.sleep(1)
sense.show_letter("!", (0, 0, r))
time.sleep(1)
sense.clear()
