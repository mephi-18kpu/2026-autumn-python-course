import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand


def integrate_simpson(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    n = len(nodes) - 1
    if n % 2 != 0:
        raise ValueError
    h = (nodes[-1] - nodes[0]) / n
    result = function(float(nodes[0])) + function(float(nodes[-1]))
    for i in range(1, n):
        if i % 2 == 1:
            result += 4.0 * function(float(nodes[i]))
        else:
            result += 2.0 * function(float(nodes[i]))
    return (result * h) / 3

