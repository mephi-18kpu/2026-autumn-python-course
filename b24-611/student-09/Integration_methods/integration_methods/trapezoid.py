# System imports

# External imports
from .type_alliases import *

# User imports

#############################################

def integrate_trapezoid(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    res = 0
    for i in range(0, len(nodes) - 1):
        res += (function(nodes[i + 1]) + function(nodes[i])) * (nodes[i + 1] - nodes[i])/2
    return res

