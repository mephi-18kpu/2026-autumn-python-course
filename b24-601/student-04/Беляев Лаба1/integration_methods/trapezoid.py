import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand

def integrate_trapezoid(nodes: NDArray[np.float64], function: Integrand) -> float:
    h = nodes[1] - nodes[0]
    f_start = function(nodes[0])
    f_end = function(nodes[-1])

    # Тут неправильно вычисляешь площадь под трапецией
    f_internal = np.sum([function(x) for x in nodes[1:-1]])

    return float(h * ((f_start + f_end) / 2.0 + f_internal))
