# Stops all motors.
#
# Authors:
#   Filip Smola

import ev3dev.ev3 as ev3

motors = ['outA', 'outB', 'outC', 'outD']

for m in motors:
    ev3.LargeMotor(m).stop()
