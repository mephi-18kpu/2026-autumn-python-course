from typing import List
from .type_aliases import Integrand, IntegrationMethod
from numpy.typing import NDArray
import numpy as np
def integrate_trapezoid(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    ans = 0
    h = nodes[1] - nodes[0]
    for i in range(nodes.size-1):
        ans += (function(nodes[i])+function(nodes[i]+h))/2
    ans *= h
    return ans
