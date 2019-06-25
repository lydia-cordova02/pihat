#!/usr/bin/env python
# script will show scrolling message on Pi HAT
from sense_hat import SenseHat
sense = SenseHat()


# send text Hello World! to show_message() function
sense.show_message("waddup")
