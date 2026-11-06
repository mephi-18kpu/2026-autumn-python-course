"""Метод Симпсона."""

import numpy as np
from numpy.typing import NDArray

from .type_aliases import Integrand


def integrate_simpson(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    #Интеграл составным методом Симпсона
    if nodes.ndim != 1:
        raise ValueError("Узлы должны быть одномерным массивом")

    if len(nodes) < 3 or len(nodes) % 2 == 0:
        raise ValueError("Нужно нечётное число узлов (не меньше трёх)")

    steps = np.diff(nodes)

    if np.any(steps <= 0):
        raise ValueError("Узлы должны идти строго по возрастанию")

    if not np.allclose(steps, steps[0]):
        raise ValueError("Метод Симпсона в этой реализации требует равномерную сетку")

    step = float(steps[0])

    total = function(float(nodes[0])) + function(float(nodes[-1]))

    for i in range(1, len(nodes) - 1):
        if i % 2 == 1:
            total += 4.0 * function(float(nodes[i]))
        else:
            total += 2.0 * function(float(nodes[i]))

    return float(total * step / 3.0)
#Метод симпсона я не оч понял, поэтому завайбил)
