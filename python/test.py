#!/usr/bin/python3

from L298NHBridge import *
from time import sleep

# pin setup
ENA = 2
IN1 = 3
IN2 = 4
IN3 = 16
IN4 = 26
ENB = 21

print("Running Motor")

bridge = L298NHBridge(ENA, IN1, IN2, IN3, IN4, ENB)

speed = 1.0

while True:
    if speed > 0.0:
        print("turning forward")
    else:
        print("turning backward")

    speed *= -1.0
    bridge.setMotors(speed, speed)
    sleep(2)

