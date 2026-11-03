# System imports

# External imports
from .type_alliases import *

# User imports

#############################################

def integrate_simpson(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    res=0
    if len(nodes)%2==0:
        return float('nan')
    else:
        for i in range(0, len(nodes) - 2, 2):
            res += (function(nodes[i + 2]) + 4 * function((nodes[i + 1])) + function(nodes[i])) * (nodes[i + 1] - nodes[i])/3
        return res
