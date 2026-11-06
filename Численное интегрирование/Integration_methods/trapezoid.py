import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand

def integrate_trapezoid(nodes: NDArray[np.float64],function: Integrand,) -> float:
    i = 0
    h = nodes[1] - nodes[0]
    for j in range(len(nodes) - 1):
        i += ((function(nodes[j])+function(nodes[j+1]))/2)*h
    return i