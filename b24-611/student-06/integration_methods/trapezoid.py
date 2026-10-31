import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand

def integrate_trapezoid(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    integral4 = 0
    for index in range(len(nodes)-1):
        integral4 += (nodes[index + 1] - nodes[index]) * (function(nodes[index])+function(nodes[index+1]))/2
    return float(integral4)
