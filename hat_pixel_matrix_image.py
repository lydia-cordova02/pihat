#!/usr/bin/env python
# script will display colors for indiv pixels
from sense_hat import SenseHat
import time
sense = SenseHat()
b = (0, 0, 0)
w = (255, 255, 255)

pixels = [
    b, b, b, b, b, b, b, b, 
    b, w, w, w, w, w, w, b, 
    b, w, b, b, b, b, w, b, 
    b, w, b, w, w, b, w, b, 
    b, w, b, w, w, b, w, b, 
    b, w, b, b, b, b, w, b, 
    b, w, w, w, w, w, w, b,
    b, b, b, b, b, b, b, b,
]

sense.set_pixels(pixels)
time.sleep(0.5)

pixels = [
    w, w, w, w, w, w, w, w, 
    w, b, b, b, b, b, b, w, 
    w, b, w, w, w, w, b, w, 
    w, b, w, b, b, w, b, w, 
    w, b, w, b, b, w, b, w,
    w, b, w, w, w, w, b, w, 
    w, b, b, b, b, b, b, w, 
    w, w, w, w, w, w, w, w, 
]

sense.set_pixels(pixels)
time.sleep(0.5)
sense.clear()
