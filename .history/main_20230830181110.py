#!/usr/bin/env python3
from ev3dev2.sensor.lego import TouchSensor
print("hi")
ts = TouchSensor()
while True:
    if ts.is_pressed():
        print("Pressed")
    else:
        pass