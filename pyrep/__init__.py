import os
try:
    os.environ["VREP_LIBRARY"]
except KeyError:
    if os.path.exists("/usr/share/vrep/"):
        os.environ["VREP_LIBRARY"] = "/usr/share/vrep/"
    else:
        raise OSError("Can't find V-Rep share folder")
if not os.path.exists(os.environ["VREP_LIBRARY"]):
    raise OSError(
        "V-Rep library directory {} does not exist!".format(
            os.environ["VREP_LIBRARY"]))
del os
from .api import VRepApi as VRep
