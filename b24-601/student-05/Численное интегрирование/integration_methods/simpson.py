from typing import List
from .type_aliases import Integrand, IntegrationMethod
from numpy.typing import NDArray
import numpy as np
def integrate_simpson(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    ans = 0
    h = nodes[1] - nodes[0]
    for i in range(1,nodes.size - 1,2):
        ans+=(function(nodes[i-1]) + 4*function(nodes[i])+function(nodes[i+1]))
    ans*=h/3
    return ans
