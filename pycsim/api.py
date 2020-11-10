import sim as s
import simConst as sc
from .common import ReturnCommandError
from .joints import Joints
from .sensors import Sensors
from .simulationstate import SimulationState
from .shapes import Shapes


class CSimApi:
    def __init__(self, id):
        self._id = id
        self.joint = Joints(id)  # type: Joints
        self.sensor = Sensors(id)  # type: Sensors
        self.simulation = SimulationState(id)  # type: SimulationState
        self.shape = Shapes(id)  # type : Shape

    @staticmethod
    def connect(ip, port):
        res = s.simxStart(
            connectionAddress=ip,
            connectionPort=port,
            waitUntilConnected=True,
            doNotReconnectOnceDisconnected=True,
            timeOutInMs=5000,
            commThreadCycleInMs=5)
        if res == sc.simx_return_ok:
            return CSimApi(res)
        else:
            raise ReturnCommandError(res)
            
    def close_connection(self):
        s.simxFinish(self._id)

    def __enter__(self):
        self.simulation.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.simulation.stop()
        self.close_connection()
