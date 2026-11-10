"""Метод Симпсона (метод парабол)."""

# System imports

# External imports
import numpy as np
from numpy.typing import NDArray

# User imports
from .type_aliases import Integrand

#############################################


def integrate_simpson(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Вычислить интеграл составным методом Симпсона."""
    if nodes.ndim != 1:
        raise ValueError("Массив узлов должен быть одномерным.")
    if nodes.size < 3:
        raise ValueError("Для метода Симпсона нужно не менее трёх узлов.")
    if nodes.size % 2 == 0:
        raise ValueError("Для метода Симпсона требуется нечётное число узлов.")

    differences = np.diff(nodes)
    if np.any(differences <= 0):
        raise ValueError("Узлы должны строго возрастать.")

    step = float(differences[0])
    if not np.allclose(differences, step):
        raise ValueError("Сетка должна быть равномерной.")

    values = [function(float(node)) for node in nodes]
    weighted_sum = (
        values[0]
        + 4.0 * sum(values[1:-1:2])
        + 2.0 * sum(values[2:-1:2])
        + values[-1]
    )
    return float(step * weighted_sum / 3.0)
