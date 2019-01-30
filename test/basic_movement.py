# Runs the motors back for 6 seconds and forward at 6 seconds.
# Used to test basic movement and accuracy of arch on base frame.
#
# Authors:
# Jeremy Scott
# Filip Smola

import ev3dev.ev3 as ev3
import time

def forward_and_back():
    print("forward_and_back entry")

    motorA = ev3.LargeMotor('outA')
    motorA.connected

    motorB = ev3.LargeMotor('outB')
    motorB.connected

    #Run both motors forward.
    motorA.run_timed(speed_sp=-100, time_sp=6000)
    motorB.run_timed(speed_sp=-100, time_sp=6000)

    #Prevent progression until the motors have stopped moving forward.
    #waitForMotor(motorA, motorB)
    motorA.wait_while('running')
    motorB.wait_while('running')

    #Run both motors backward.
    motorA.run_timed(speed_sp=100, time_sp=6000)
    motorB.run_timed(speed_sp=100, time_sp=6000)

    motorA.wait_while('running')
    motorB.wait_while('running')

# def waitForMotor(motorA, motorB):
    # time.sleep(0.1)         # Make sure that motor has time to start
    # while (motorA.state==["running"] | motorB.state==["running"]):
        # print('Motor is still running')
        # time.sleep(0.1)

for i in range(1,5):
    print(i)
    forward_and_back()
