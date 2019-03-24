# Implementation of the Low Level Interface for the EV3 resume button.
#
# Author(s):
#   Filip Smola

import ev3dev.ev3 as ev3

class Button:
    # True iff the resume button is pressed
    def pressed(self):
        return ev3.Button.enter
