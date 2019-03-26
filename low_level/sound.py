# Implementation of the Low Level Interface for the EV3 sound system
#
# Author(s):
#   Filip Smola

import ev3dev.ev3 as ev3

class Sound:
    # Beep
    def beep(self):
        return ev3.Sound.beep()
