import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand


def integrate_trapezoid(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    h = nodes[1] - nodes[0]
    s = h * (function(nodes[0])/2 + sum(function(node) for node in nodes[1:-1]) + function(nodes[-1])/2)
    return s
