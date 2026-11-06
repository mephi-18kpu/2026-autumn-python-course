import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand


def integrate_simpson(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    if len(nodes) % 2 == 0:
        raise ValueError("Для метода Симпсона нужно нечётное число узлов")
    h = nodes[1] - nodes[0]
    s = h/3 * (function(nodes[0]) + 4 * sum(function(node) for node in nodes[1:-1:2]) + 2 * sum(function(node) for node in nodes[2:-1:2]) + function(nodes[-1]))
    return s
