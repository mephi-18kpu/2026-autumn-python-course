import numpy as np
from numpy.typing import NDArray
from .type_integration import Integrand

def integrate_trapezoid(
    nodes: NDArray[np.float64], function: Integrand
) -> float:
    h = nodes[1] - nodes[0]
    total = 0.0

    for i in range(len(nodes) - 1):
        left = function(float(nodes[i]))
        right = function(float(nodes[i + 1]))
        average_height = (left + right) / 2
        area = h * average_height
        total = total + area
    return float(total)
