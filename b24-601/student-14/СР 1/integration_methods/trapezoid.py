"""Трапеции"""

import numpy as np
from numpy.typing import NDArray

from .type_aliases import Integrand


def integrate_trapezoid(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    #Интеграл методом трапеций
    if nodes.ndim != 1 or len(nodes) < 2:
        raise ValueError
    if np.any(np.diff(nodes) <= 0):
        raise ValueError

    total = 0.0

    for i in range(len(nodes) - 1):
        step = float(nodes[i + 1] - nodes[i])
        left_value = function(float(nodes[i]))
        right_value = function(float(nodes[i + 1]))
        total += (left_value + right_value) * step / 2.0

    return float(total)
