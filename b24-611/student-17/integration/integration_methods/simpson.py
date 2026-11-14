import numpy as np
from numpy.typing import NDArray
from .type_integration import Integrand

def integrate_simpson(
    nodes: NDArray[np.float64], function: Integrand
) -> float:
    h = nodes[1] - nodes[0]
    total = 0.0

    for i in range(0, len(nodes) - 2, 2):
        left = function(float(nodes[i]))
        middle = function(float(nodes[i + 1]))
        right = function(float(nodes[i + 2]))
        area = h / 3 * (left + 4 * middle + right)
        total = total + area
    return float(total)
