
from typing import Callable
from numpy.typing import NDArray
import numpy as np

Integrand = Callable[[float], float]
IntegrationMethod = Callable[[NDArray[np.float64], Integrand], float]