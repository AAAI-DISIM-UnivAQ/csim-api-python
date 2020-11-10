import time
from pycsim import CSim
from math import *
# contextlib
# simpy
# multiprocessing cpu


with CSim.connect("127.0.0.1", 19997) as csim:
#    csim.simulation.stop()
#    time.sleep(2)
#    csim.simulation.start()

    j_vel = csim.joint.with_velocity_control("joint_force")
    j_pos = csim.joint.with_position_control("joint_position")
    j_pas = csim.joint.passive("joint_passive")
    j_sph = csim.joint.spherical("sp_joint")
    j_spr = csim.joint.spring("joint_spring")

    s = csim.sensor.proximity("sensor")
    v = csim.sensor.vision("vision")

    j_vel.set_target_velocity(2)
    j_spr.set_target_position(2)
    
    for i in range(5):
        b = pi / 9
        j_pos.set_target_position(b * i + 0.2)
        time.sleep(1)
    for i in range(50):
        v = sin(i / 10)
        j_pas.set_position(v)
        time.sleep(0.1)

    for i in range(1000):
        v = sin(i / 100) * (i / 1000)
        j_sph.set_matrix(
            [0, 0, 0, 0,
             0, 0, 0, 0,
             v, 0, 0, 0])
        time.sleep(0.01)


# csim.simulation.stop()

