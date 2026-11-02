from .type_aliases import Integrand
from numpy.typing import NDArray
import numpy as np

def integrate_simpson(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    sumi1 = 4 * sum(function(x) for x in nodes[1:-1:2])
    sumi2 = 2 * sum(function(x) for x in nodes[2:-1:2])
    h = nodes[1] - nodes[0]
    return float((h/3)*(function(nodes[0]) + sumi1
                        + sumi2 + function(nodes[-1])))
