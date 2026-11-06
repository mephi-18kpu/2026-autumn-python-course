import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand

def integrate_trapezoid(nodes: NDArray[np.float64], function: Integrand, ) -> float:
    if len(nodes) < 2:
        raise ValueError("минимум 2 точки")

    h = nodes[1] - nodes[0]
    n = len(nodes)

    edges = (function(nodes[0]) + function(nodes[-1])) / 2

    integral_sum = sum(function(x) for x in nodes[1:-1])

    return float(h * (edges + integral_sum))

