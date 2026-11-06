import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand

def integrate_trapezoid(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    h = nodes[1] - nodes[0]
    total_sum = 0.5 * function(nodes[0]) + 0.5 * function(nodes[-1])
    for i in range(1, len(nodes) - 1):
        total_sum += function(nodes[i])
    return float(h * total_sum)