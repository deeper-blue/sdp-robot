# A test to lower the robot arm up and down.
# Author(s)
#    Jeremy Scott

import ev3dev.ev3 as ev3
import time
import math
import motor

def iteration():
    # Get motor
    #motorD = motor.Single(motor.portD)
    motorD = ev3.LargeMotor('outD')

    # Test run of the motor for 5 second
    # Positive speed = higher arm AND negative speed = lower arm
    motorD.run_timed(speed_sp = 500, time_sp = 5000)
    motorD.wait_while('running')
    motorD.run_timed(speed_sp = -500, time_sp = 5000)
    motorD.wait_while('running')

for i in range(1,4):
    iteration()
