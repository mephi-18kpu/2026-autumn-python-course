# System imports
from typing import Callable

# External imports
import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand

# User imports

#############################################


def integrate_left_rectangles(nodes: NDArray[np.float64], function: Integrand) -> float:
    h = nodes[1] - nodes[0]
    total = 0.0

    for i in range(len(nodes) - 1):
        total += function(nodes[i]) * h

    return total

def integrate_right_rectangles(nodes: NDArray[np.float64], function: Integrand) -> float:
    h = nodes[1] - nodes[0]
    total = 0.0

    for i in range(1, len(nodes)):
        total += function(nodes[i]) * h

    return total


def integrate_midpoint_rectangles(nodes: NDArray[np.float64], function: Integrand) -> float:
    h = nodes[1] - nodes[0]
    total = 0.0

    for i in range(len(nodes) - 1):
        x = nodes[i] + h / 2
        total += function(x) * h

    return total
