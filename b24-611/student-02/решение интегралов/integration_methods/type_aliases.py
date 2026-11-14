from typing import Callable

import numpy as np
from numpty.typing import NDArray

Integrand = Callable[[float], float]
IntegrationMethod = Callable[[NDArray[np.float64], Integrand], float]
