"""Метод численного интегрирования Симпсона."""

import numpy as np
from numpy.typing import NDArray

from .type_aliases import Integrand


def integrate_simpson(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Вычисляет интеграл методом Симпсона."""
    if nodes.ndim != 1 or nodes.size < 3 or nodes.size % 2 == 0:
        raise ValueError(
            "Для метода Симпсона нужно нечётное число узлов: не менее трёх."
        )

    differences = np.diff(nodes)

    if np.any(differences <= 0):
        raise ValueError("Узлы сетки должны строго возрастать.")

    step = float(differences[0])

    if not np.allclose(differences, step):
        raise ValueError("Узлы сетки должны быть расположены равномерно.")

    # Вычисляем значения функции во всех узлах.
    values = np.array(
        [function(float(x)) for x in nodes],
        dtype=np.float64,
    )

    # Нечётные внутренние индексы умножаются на 4,
    # чётные внутренние индексы — на 2.
    weighted_sum = (
        values[0]
        + 4.0 * np.sum(values[1:-1:2])
        + 2.0 * np.sum(values[2:-1:2])
        + values[-1]
    )

    return float(step * weighted_sum / 3.0)
