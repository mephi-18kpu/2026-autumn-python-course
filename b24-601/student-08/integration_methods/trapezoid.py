import numpy as np
from numpy.typing import NDArray

from .type_aliases import Integrand


def integrate_trapezoid(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    h = nodes[1] - nodes[0]
    total = 0.0
    for i in range(len(nodes) - 1):
        total += (function(float(nodes[i])) + function(float(nodes[i + 1]))) / 2.0
    return float(h * total)
