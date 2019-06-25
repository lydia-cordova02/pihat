#!/usr/bin/env python
# script will display colors for indiv pixels
from sense_hat import SenseHat
sense = SenseHat()
import time

import random

# r = random integer between 0-7
r = random.randint(0, 7)

sense.set_pixel(r, r, (255, 255, 0))

time.sleep(1)
sense.clear()
