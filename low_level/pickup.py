# Implementation of the Low Level Interface for the Pickup Sensor.
#
# Author(s):
#   Filip Smola

from . import config
import ev3dev.ev3 as ev3

class Pickup:
    # Construct pickup sensor by instantiating the ultrasonic sensor
    def __init__(self):
        # Set the sensor
        self.sensor = ev3.UltrasonicSensor(config.pickup_sensor)

    # Return True iff a piece is picked up (present in front of sensor), False otherwise
    def present(self):
        dist = self.sensor.distance_centimeters
        if dist <= config.pickup_threshold:
            print("Pickup Sensor: piece is present")
            return True
        else:
            print("Pickup Sensor: piece is absent")
            return False

    # Return False iff a piece is picked up (present in front of sensor), True otherwise
    def absent(self):
        return not self.present()
