"""Метод численного интегрирования составными трапециями."""

import numpy as np
from numpy.typing import NDArray

from .type_aliases import Integrand


def integrate_trapezoid(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Вычисляет интеграл методом трапеций."""
    if nodes.ndim != 1 or nodes.size < 2:
        raise ValueError("Сетка должна быть одномерной и содержать не менее двух узлов.")

    differences = np.diff(nodes)

    if np.any(differences <= 0):
        raise ValueError("Узлы сетки должны строго возрастать.")

    step = float(differences[0])

    if not np.allclose(differences, step):
        raise ValueError("Узлы сетки должны быть расположены равномерно.")

    # Вычисляем значения функции во всех узлах сетки.
    values = np.array(
        [function(float(x)) for x in nodes],
        dtype=np.float64,
    )

    # Крайние значения имеют вес 1/2, внутренние — вес 1.
    result = step * (
        0.5 * values[0]
        + np.sum(values[1:-1])
        + 0.5 * values[-1]
    )

    return float(result)
