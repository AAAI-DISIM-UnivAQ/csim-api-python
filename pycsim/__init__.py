import os
try:
    os.environ["CSIM_LIBRARY"]
except KeyError:
    if os.path.exists("/usr/share/csim/"):
        os.environ["CSIM_LIBRARY"] = "/usr/share/csim/"
    else:
        raise OSError("Can't find CSIM share folder")
if not os.path.exists(os.environ["CSIM_LIBRARY"]):
    raise OSError(
        "CSIM library directory {} does not exist!".format(
            os.environ["CSIM_LIBRARY"]))
import sys
sys.path.append(os.environ["CSIM_LIBRARY"])
del os
from .api import CSimApi as CSim
