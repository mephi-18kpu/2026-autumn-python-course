import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand

def integrate_simpson(nodes: NDArray[np.float64],function: Integrand,) -> float:
    i = 0
    h = nodes[1] - nodes[0]
    for j in range(0,len(nodes) - 2,2):
        i += ((function(nodes[j]) + 4*function(nodes[j + 1]) + function(nodes[j + 2])) / 3) * h
    return i