import numpy as np
from numpy.typing import NDArray

from .type_aliases import Integrand

def integrate_simpson(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    if nodes.ndim != 1 or len(nodes) < 3 or len(nodes) % 2 == 0:
        raise ValueError("Для Симпсона нужно нечётное число узлов, минимум три.")

    h = float(nodes[1] - nodes[0])
    total = function(float(nodes[0])) + function(float(nodes[-1]))
    for i in range(1, len(nodes) - 1):
        if i % 2 == 1:
            total += 4.0 * function(float(nodes[i]))
        else:
            total += 2.0 * function(float(nodes[i]))
    return float(h * total / 3.0)
