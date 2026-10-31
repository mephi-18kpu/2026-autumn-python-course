from typing import Callable
import numpy as np
from numpy.typing import NDArray

Integrand = Callable[[float], float]
IntegrationMethod = Callable[[NDArray[np.float64], Integrand], float]
