# System imports
from typing import Callable

# External imports
import numpy as np
from numpy.typing import NDArray

# User imports

#############################################

def integrate_simpson(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    ...
