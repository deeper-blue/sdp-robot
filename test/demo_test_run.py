# Run tests, wait for ev3 button pressed before starting each test.
# Author(s)
#    Jeremy Scott

import ev3dev.ev3 as ev3
import time
import math
import motor
import move

# Wheel circumference
circ = 12.9 # in cm

def iteration1():
    print("iteration entry")

    # Get twin motors
    twins = motor.Twin(motor.portA, motor.portB)

    # Prepare movement
    movement = move.Uniform(circ)

    # Move forward by 50 cm and back
    movement.move(twins, -50)
    movement.move(twins,  50)

def iteration2():
    print("iteration entry")

    # Get twin motors
    twins = motor.Twin(motor.portA, motor.portB)

    # Prepare movement
    movement = move.Gradual(circ)

    # Move forward by 50 cm and back
    movement.move(twins, -50)
    movement.move(twins,  50)

def iteration3():
    print("iteration entry")

    # Get motor
    motorC = motor.Single(motor.portC)

    # Prepare movement
    movement = move.Uniform(circ)
    movement.speed_long = 200

    # Move long distance
    movement.move(motorC, 25)
    movement.move(motorC, -50)
    movement.move(motorC, 25)

btn = ev3.Button()

iteration1()

while not btn.any():
    time.sleep(0.01)

time.sleep(1)

iteration2()

while not btn.any():
    time.sleep(0.01)

time.sleep(1)

iteration3()
