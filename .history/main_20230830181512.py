#!/usr/bin/env python3

from time import sleep

from ev3dev2.led import Leds
from ev3dev2.sensor.lego import TouchSensor

ts = TouchSensor()
leds = Leds()

print("Press the touch sensor to change the LED color!")
timeout = 0

while True:
    if ts.is_pressed:
        leds.set_color("LEFT", "GREEN")
        leds.set_color("RIGHT", "GREEN")
        print("pressed")
        timeout += 1
    else:
        leds.set_color("LEFT", "RED")
        leds.set_color("RIGHT", "RED")
        timeout = 0
    # don't let this loop use 100% CPU
    sleep(0.01)