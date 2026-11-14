import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand


def integrate_trapezoid(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    h = nodes[1] - nodes[0]
    total = 0.5*function(nodes[0]) + 0.5*function(nodes[-1])
    for x in nodes[1:-1]:
        total += function(x)

    return float(h * total)
