import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand

def integrate_simpson(
        nodes: NDArray[np.float64],
        function: Integrand,
) -> float:
    n = len(nodes) - 1
    if n % 2 != 0:
        raise ValueError("Число интервалов n должно быть четным.")

    h = nodes[1] - nodes[0]
    total_sum = function(nodes[0]) + function(nodes[-1])

    for i in range(1, n):
        if i % 2 != 0:
            total_sum += 4.0 * function(nodes[i])
        else:
            total_sum += 2.0 * function(nodes[i])

    return float((h / 3.0) * total_sum)