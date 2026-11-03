# System imports
from typing import Callable

# External imports
import numpy as np
from numpy.typing import NDArray

# User imports

#############################################

def integrate_simpson(nodes: NDArray[np.float64], function: Integrand) -> float:
    h = nodes[1] - nodes[0]
    total = 0.0

    for i in range(0, len(nodes) - 2, 2):
        total += (function(nodes[i]) + 4 * function(nodes[i + 1]) + function(nodes[i + 2])) * h / 3

    return total
