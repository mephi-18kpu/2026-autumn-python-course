from .type_aliases import Integrand
from numpy.typing import NDArray
import numpy as np

def integrate_trapezoid(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    sumi = sum(function(x) for x in nodes[1:-1])
    h = nodes[1] - nodes[0]
    return float(h*(function(nodes[0])/2 + sumi + function(nodes[1])/2))
