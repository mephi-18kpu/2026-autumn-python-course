import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand

def integrate_simpson(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    integral5 = 0
    index = 0
    while index < len(nodes)-2:
        integral5 += (nodes[index + 1] - nodes[index])/3 * (function(nodes[index])+4*function(nodes[index+1])+function(nodes[index+2]))
        index += 2
    return integral5
