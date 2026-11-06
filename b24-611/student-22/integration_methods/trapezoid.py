"""Модуль реализации метода трапеций."""

# System imports

# External imports
import numpy as np
from numpy.typing import NDArray

# User imports
from .type_aliases import Integrand

#############################################


def integrate_trapezoid(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Вычисление интеграла методом трапеций.

    T_h = h * (f_0 / 2 + sum_{i=1}^{n-1} f_i + f_n / 2)
    """
    if len(nodes) < 2:
        raise ValueError("Число узлов должно быть не менее 2.")

    h = (nodes[-1] - nodes[0]) / (len(nodes) - 1)
    f_0 = function(float(nodes[0]))
    f_n = function(float(nodes[-1]))
    internal_sum = sum(function(float(x)) for x in nodes[1:-1])

    return float(h * (0.5 * f_0 + internal_sum + 0.5 * f_n))
