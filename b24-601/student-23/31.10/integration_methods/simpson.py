"""Метод Симпсона (метод парабол)."""

from numpy.typing import NDArray
import numpy as np
from .type_aliases import Integrand


def integrate_simpson(nodes: NDArray[np.float64], function: Integrand) -> float:

    n = len(nodes) - 1
    if n % 2 != 0:
        raise ValueError("Для метода Симпсона число интервалов должно быть чётным (число узлов нечётным).")

    h = nodes[1] - nodes[0]

    total = function(nodes[0]) + function(nodes[-1])

    total += 4.0 * sum(function(nodes[i]) for i in range(1, n, 2))

    total += 2.0 * sum(function(nodes[i]) for i in range(2, n, 2))

    return float((h / 3.0) * total)
