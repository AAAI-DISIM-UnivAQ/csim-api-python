# CSim python

## A Python 3.x wrapper for the Coppelia Robotics Remote API

Simple python binding for
[Coppelia SIM Robotics simulator](http://www.coppeliarobotics.com/) 
([remote API](http://www.coppeliarobotics.com/helpFiles/en/remoteApiOverview.htm)), 
tested with version **4.1.0 (rev 1 - EDU)**

## Getting started

0. Requirements: CPython version >= 3.5.2, pip
1. Install library from PyPI by entering this command:
```bash
[sudo] pip install 'git+https://github.com//AAAI-DISIM-UnivAQ/csim-api-python.git'
```

## C-Sim specific
Package needs platform-specific native library (remoteApi). 
It uses two enviroment variables `CSIM` and `CSIM_LIBRARY`. 
If `CSIM` is unspecified package will use default `/usr/share/csim` for it. 
If `CSIM_LIBRARY` is also unspecified, then it will concatenate `CSIM` with `programming/remoteApiBindings/lib/lib/64Bit/`. 
This setup is tested and develoed under **LINUX ONLY**. Mac users should not have problems.

To have everything in `/usr/share/csim` :

    sudo mkdir /usr/share/csim
    sudo cp <CSIM dir>programming/remoteApiBindings/lib/lib/Linux/64Bit/*.so /usr/share/csim/.
    sudo cp <CSIM dir>programming/remoteApiBindings/python/python/vrep*.py /usr/share/csim/.

check if the last character of the path is "/" in the environment variable value, like for example:

    export CSIM_LIBRARY=/usr/share/csim/
                                       ^^
                                       
### For Windows users:

(_NOT TESTED ENOUGH_)

define a CSIM_LIBRARY environment variable pointing to your shared vrep folder which sould include the following files:

    * remoteApi.dll (64bit for Windows 10)
    * sim.py
    * simConst.py
  
check if the last character of the path is "\\" in the environment variable value, like for example:
    
    C:\Users\<username>\csim_share\
                                  ^^

We are open for contributions to debug it under Windows.
    
To use package you will need the socket port number, which can be located in `CSIM/remoteApiConnections.txt`.

## Currently implemented things

In the current version is not implemented features such as remote management GUI,
additional configuration properties of objects and shapes, etc.
Basically implemented those components that are required to control the robot:
* Joint
* Proximity sensor
* Vision sensor
* Force sensor
* Position sensor
* Shape primitive object handle (used for shape object)
* ~~Remote function calls~~

## Example
Designed to be used with `examples/Pioneer.ttt`.
```python
from pycsim import CSim
import time

class PioneerP3DX:

    def __init__(self, api: CSim):
        self._api = api
        self._left_motor = api.joint.with_velocity_control("Pioneer_p3dx_leftMotor")
        self._right_motor = api.joint.with_velocity_control("Pioneer_p3dx_rightMotor")
        self._left_sensor = api.sensor.proximity("Pioneer_p3dx_ultrasonicSensor3")
        self._right_sensor = api.sensor.proximity("Pioneer_p3dx_ultrasonicSensor6")

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

with CSim.connect("127.0.0.1", 19997) as api:
    r = PioneerP3DX(api)
    while True:
        rl = r.right_length()
        ll = r.left_length()
        if 0.01 < rl < 10:
            r.rotate_left()
        elif 0.01 < ll < 10:
            r.rotate_right()
        else:
            r.move_forward()
        time.sleep(0.1)

```


## License
Copyright (C) 2016-2020  Stanislav Eprikov, Pavel Pletenev, Giovanni De Gasperis

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
