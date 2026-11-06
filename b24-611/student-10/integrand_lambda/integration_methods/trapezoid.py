import numpy as np
from numpy.typing import NDArray
from integration_methods.type_aliases import Integrand

def integrate_trapezoid(nodes: NDArray[np.float64], function: Integrand) -> float:
    h = float(nodes[1] - nodes[0])
    f_values = function(nodes)
    result = h * (0.5 * (f_values[0] + f_values[-1]) + np.sum(f_values[1:-1]))
    return float(result)
