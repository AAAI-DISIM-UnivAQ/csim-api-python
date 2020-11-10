import sim as s
import simConst as sc


class SimulationState:

    def __init__(self, id):
        self._id = id
        self._def_op_mode = sc.simx_opmode_oneshot_wait

    def start(self):
        s.simxStartSimulation(self._id, self._def_op_mode)

    def pause(self):
        s.simxPauseSimulation(self._id, self._def_op_mode)

    def stop(self):
        s.simxStopSimulation(self._id, self._def_op_mode)
