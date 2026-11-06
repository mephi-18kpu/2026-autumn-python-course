import numpy as np

from numpy.typing import NDArray

from .type_aliases import Integrand

def integrate_trapezoid(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    h = nodes[1] - nodes[0]
    func_val = function(nodes)

    total = np.sum(func_val[1:-1]) + 0.5*(func_val[0] + func_val[-1]) #первым не берем наружние, вторым как раз берем края
    return float(h*total)
