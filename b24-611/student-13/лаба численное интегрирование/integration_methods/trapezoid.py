# System imports
from typing import Callable

# External imports
import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand

# User imports

#############################################

def integrate_trapezoid(nodes: NDArray[np.float64], function: Integrand) -> float:
    h = nodes[1] - nodes[0]
    total = 0.0

    for i in range(len(nodes) - 1):
        total += (function(nodes[i]) + function(nodes[i + 1])) * h / 2

    return total
