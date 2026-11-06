import numpy as np
from numpy.typing import NDArray
from integration_methods.type_aliases import Integrand

def integrate_simpson(nodes: NDArray[np.float64], function: Integrand) -> float:
    h = float(nodes[1] - nodes[0])
    f_values = function(nodes)
    result = f_values[0] + f_values[-1]
    result += 4.0 * np.sum(f_values[1:-1:2])
    result += 2.0 * np.sum(f_values[2:-2:2])
    return float(result * h / 3.0)
