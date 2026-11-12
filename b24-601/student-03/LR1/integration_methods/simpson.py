import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand

def integrate_simpson(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    h = nodes[1] - nodes[0]
    integral = (h/3)*np.sum(function(nodes[:-2:2]) + 4*function(nodes[1:-1:2]) + function(nodes[2::2]))

    return float(integral)
