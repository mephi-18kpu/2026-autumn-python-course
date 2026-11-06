import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand

def integrate_simpson(nodes: NDArray[np.float64], function: Integrand) -> float:
    n = len(nodes) - 1
    if len(nodes) < 3 or n % 2 != 0:
        raise ValueError("для симпсона нечетное число узлов нужно(минимум 3)")

    h = nodes[1] - nodes[0]
    y = [function(x) for x in nodes]
    s = y[0] + y[-1]
    s += 4 * sum(y[i] for i in range(1, n, 2))

    s += 2 * sum(y[i] for i in range(2, n, 2))

    return float((h / 3) * s)
