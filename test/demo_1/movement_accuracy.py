# Runs the motors back and forth for 25 cm.
# This is repeated 20 times.
# Used to measure movement accuracy over 10 m.
#
# Authors:
#   Jeremy Scott
#   Filip Smola

import ev3dev.ev3 as ev3
import time

circ = 12.9 # in cm
dist = 25   # in cm
rots = dist / circ
pos = rots * 360

speed = 200

ramp_pos_factor = 0.1
ramp_speed_factor = 0.5

main_pos_factor = 1 - (2 * ramp_pos_factor)
main_speed_factor = 1

def move(polarity, motorA, motorB):
    # Ramp up
    motorA.run_to_rel_pos(speed_sp= polarity * (ramp_speed_factor * speed), position_sp = polarity * (ramp_pos_factor * pos))
    motorB.run_to_rel_pos(speed_sp= polarity * (ramp_speed_factor * speed), position_sp = polarity * (ramp_pos_factor * pos))

    # Wait for completion
    motorA.wait_while('running')
    motorB.wait_while('running')

    # Run main part
    motorA.run_to_rel_pos(speed_sp= polarity * (main_speed_factor * speed), position_sp = polarity * (main_pos_factor * pos))
    motorB.run_to_rel_pos(speed_sp= polarity * (main_speed_factor * speed), position_sp = polarity * (main_pos_factor * pos))

    # Wait for completion
    motorA.wait_while('running')
    motorB.wait_while('running')

    # Ramp down
    motorA.run_to_rel_pos(speed_sp= polarity * (ramp_speed_factor * speed), position_sp = polarity * (ramp_pos_factor * pos))
    motorB.run_to_rel_pos(speed_sp= polarity * (ramp_speed_factor * speed), position_sp = polarity * (ramp_pos_factor * pos))

    # Wait for completion
    motorA.wait_while('running')
    motorB.wait_while('running')


def iteration():
    print("iteration entry")

    motorA = ev3.LargeMotor('outA')
    motorA.connected

    motorB = ev3.LargeMotor('outB')
    motorB.connected

    move(-1, motorA, motorB)
    move(1, motorA, motorB)

for i in range(1,20):
    print(i)
    iteration()
