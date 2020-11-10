from pycsim import CSim, common
import time


class PioneerP3DX:

    def __init__(self, api: CSim):
        self._api = api
        self._left_motor = api.joint.with_velocity_control("Pioneer_p3dx_leftMotor")
        self._right_motor = api.joint.with_velocity_control("Pioneer_p3dx_rightMotor")
        self._left_sensor = api.sensor.proximity("Pioneer_p3dx_ultrasonicSensor3")
        self._right_sensor = api.sensor.proximity("Pioneer_p3dx_ultrasonicSensor6")
        self._debug_shape = api.shape.primitive("debug")

    def rotate_right(self, speed=2.0):
        self._set_two_motor(speed, -speed)

    def rotate_left(self, speed=2.0):
        self._set_two_motor(-speed, speed)

    def move_forward(self, speed=2.0):
        self._set_two_motor(speed, speed)

    def move_backward(self, speed=2.0):
        self._set_two_motor(-speed, -speed)

    def _set_two_motor(self, left: float, right: float):
        self._left_motor.set_target_velocity(left)
        self._right_motor.set_target_velocity(right)

    def right_length(self):
        return self._right_sensor.read()[1].distance()

    def left_length(self):
        return self._left_sensor.read()[1].distance()


if __name__ == "__main__":
    with CSim.connect("127.0.0.1", 19997) as api:
        #api.simulation.start()
        try:
            r = PioneerP3DX(api)
        except common.NotFoundComponentError as e:
            print(e)
            print("Have you opened the right scene inside Coppelia SIM?")
            exit(-1)
        while True:
            rl = r.right_length()
            ll = r.left_length()
            if 0.01 < rl  < 10:
                r.rotate_left()
            elif 0.01 < ll < 10:
                r.rotate_right()
            else:
                r.move_forward()
            time.sleep(0.1)

    #api.simulation.stop()



