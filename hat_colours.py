#!/usr/bin/env python
# script will define colors for scrolling message on Pi HAT
from sense_hat import SenseHat
sense = SenseHat()

#use colore values to define colors 
black = (0, 0, 0)
cyan = (0, 255, 255)

speed = 0.05

message = "waddup my names jared im 19 and i never learned how to read" 
sense.show_message(message, speed, text_colour=black, back_colour=black)

sense.clear()
