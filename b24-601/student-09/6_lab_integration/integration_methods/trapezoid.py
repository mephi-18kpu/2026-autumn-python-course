"""Метод трапеций."""

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
    """Вычислить интеграл составным методом трапеций."""
    if nodes.ndim != 1:
        raise ValueError("Массив узлов должен быть одномерным.")
    if nodes.size < 2:
        raise ValueError("Для метода трапеций нужно не менее двух узлов.")

    differences = np.diff(nodes)
    if np.any(differences <= 0):
        raise ValueError("Узлы должны строго возрастать.")

    step = float(differences[0])
    if not np.allclose(differences, step):
        raise ValueError("Сетка должна быть равномерной.")

    values = [function(float(node)) for node in nodes]
    weighted_sum = values[0] / 2.0 + sum(values[1:-1]) + values[-1] / 2.0
    return float(step * weighted_sum)
