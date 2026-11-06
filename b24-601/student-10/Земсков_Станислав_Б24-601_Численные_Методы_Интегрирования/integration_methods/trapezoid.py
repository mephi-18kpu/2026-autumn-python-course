"""Метод трапеций."""

import numpy as np
from numpy.typing import NDArray

from .type_aliases import Integrand


def integrate_trapezoid(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Сложить площади трапеций между соседними узлами."""
    if nodes.ndim != 1 or len(nodes) < 2:
        raise ValueError("Нужна одномерная сетка минимум из двух узлов.")

    h = float(nodes[1] - nodes[0])
    total = function(float(nodes[0])) / 2.0
    total += function(float(nodes[-1])) / 2.0
    for i in range(1, len(nodes) - 1):
        total += function(float(nodes[i]))
    return float(h * total)
