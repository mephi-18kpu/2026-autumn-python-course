import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand

def integrate_simpson(nodes: NDArray[np.float64], function: Integrand) -> float:
    n = len(nodes) - 1
    if n % 2 != 0:
        raise ValueError("Для метода Симпсона число интервалов должно быть четным")

    h = nodes[1] - nodes[0]
    f_0 = function(nodes[0])
    f_n = function(nodes[-1])

    # Красиво
    sum_odd = np.sum([function(nodes[i]) for i in range(1, n, 2)])
    sum_even = np.sum([function(nodes[i]) for i in range(2, n, 2)])

    result = (h / 3.0) * (f_0 + 4 * sum_odd + 2 * sum_even + f_n)
    return float(result)
