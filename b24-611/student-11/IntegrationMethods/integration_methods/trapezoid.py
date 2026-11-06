import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand


def integrate_trapezoid(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    n = len(nodes) - 1
    h = (nodes[-1] - nodes[0]) / n
    result = (function(float(nodes[0])) + function(float(nodes[-1]))) / 2
    for i in range(1, n):
        result += function(float(nodes[i]))
    return float(result * h)
