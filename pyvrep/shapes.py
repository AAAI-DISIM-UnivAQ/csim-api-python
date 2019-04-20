from .vrep import vrep as v
from .vrep import vrepConst as vc
from .common import MatchObjTypeError, NotFoundComponentError


class PrimitiveShape:

    def __init__(self, id, handle):
        self._id = id
        self._handle = handle
        self._def_op_mode = v.simx_opmode_oneshot_wait

    def set_color(self, colname):
        v.simxSetObjectIntParameter(self._id, self._handle, 3120, colname)


class Shapes:

    def __init__(self, id):
        self._id = id
        self._def_op_mode = v.simx_opmode_oneshot_wait

    def primitive(self, name: str) -> PrimitiveShape:
        handle = self._get_object_handle(name)
        if handle is not None:
            if self._check_object_type(handle, vc.sim_object_shape_type):
                return PrimitiveShape(self._id, handle)
            else:
                raise MatchObjTypeError(name)
        else:
            raise NotFoundComponentError(name)

    def _get_shape(self, name, shape_type, ctr):
        handle = self._get_object_handle(name)
        if handle is not None:
            if self._check_object_type(handle, shape_type):
                return ctr(self._id, handle)
            else:
                raise MatchObjTypeError(name)
        else:
            raise NotFoundComponentError(name)

    def _check_object_type(self, handle, obj_type):
        code, handles, _, _, _ = v.simxGetObjectGroupData(
            self._id, obj_type, 0, self._def_op_mode)
        return handles.__contains__(handle)

    def _get_object_handle(self, name):
        code, handle = v.simxGetObjectHandle(self._id, name, self._def_op_mode)
        if code == v.simx_return_ok:
            return handle
        else:
            return None

