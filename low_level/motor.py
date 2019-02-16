# Various motor abstractions used by the tests.
#
# Authors:
#   Filip Smola

import ev3dev.ev3 as ev3

# Port strings
portA = 'outA'
portB = 'outB'
portC = 'outC'
portD = 'outD'

# Two motors to be moved the same.
# The first motor is the main, second is the slave.
class Twin:
    # Construct using port strings
    def __init__(self, main, slave):
        print("Motors twinned from main %s and slave %s" % (main, slave))

        # Create motors
        self.main = ev3.LargeMotor(main)
        self.slave = ev3.LargeMotor(slave)

        # Brake on stop
        self.main.stop_action = self.main.STOP_ACTION_BRAKE
        self.slave.stop_action = self.slave.STOP_ACTION_BRAKE

        # Set motor name
        self.name = "[%s,%s]" % (main, slave)

    # Whether both motors are connected
    def connected(self):
        return self.main.connected and self.slave.connected

    # Get main motor position
    def get_position(self):
        return self.main.position

    # Delegate to both motors
    def run_direct(self, duty_cycle):
        self.main.run_direct(duty_cycle_sp = duty_cycle)
        self.slave.run_direct(duty_cycle_sp = duty_cycle)

    # Delegate to both motors
    def run_to_rel_pos(self, position, speed):
        self.main.run_to_rel_pos(position_sp = position, speed_sp = speed)
        self.slave.run_to_rel_pos(position_sp = position, speed_sp = speed)

    # Stop both motors
    def stop(self):
        self.main.stop()
        self.slave.stop()

    # Wait while motors in state
    def wait_while(self, state):
        self.main.wait_while(state)
        self.slave.wait_while(state)

# Single motor.
# Meant to unify interface with Twin.
class Single:
    # Construct using port string
    def __init__(self, motor):
        print("Motor created from %s" % (motor))

        # Create motor
        self.motor = ev3.LargeMotor(motor)

        # Brake on stop
        self.motor.stop_action = self.motor.STOP_ACTION_BRAKE

        # Set motor name
        self.name = "[%s]" % motor

    # Whether motor is connected
    def connected(self):
        return self.motor.connected

    # Get motor position
    def get_position(self):
        return self.motor.position

    # Delegate to motor
    def run_direct(self, duty_cycle):
        self.motor.run_direct(duty_cycle_sp = duty_cycle)

    # Delegate to motor
    def run_to_rel_pos(self, position, speed):
        self.motor.run_to_rel_pos(position_sp = position, speed_sp = speed)

    # Stop motor
    def stop(self):
        self.motor.stop()

    # Wait while motor in state
    def wait_while(self, state):
        self.motor.wait_while(state)
