
# System imports
from typing import Callable

# External imports
import numpy as np
from numpy.typing import NDArray

# User imports

#############################################


Integrand = Callable[[float], float]
IntegrationMethod = Callable[[NDArray[np.float64], Integrand], float]
