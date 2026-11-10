"""Методы левых, правых и средних прямоугольников."""

import numpy as np
from numpy.typing import NDArray

from .type_aliases import Integrand


def _validate_nodes(nodes: NDArray[np.float64]) -> float:
    """Проверяет сетку и возвращает её шаг."""
    if nodes.ndim != 1 or nodes.size < 2:
        raise ValueError("Сетка должна быть одномерной и содержать не менее двух узлов.")

    differences = np.diff(nodes)

    if np.any(differences <= 0):
        raise ValueError("Узлы сетки должны строго возрастать.")

    step = float(differences[0])

    if not np.allclose(differences, step):
        raise ValueError("Узлы сетки должны быть расположены равномерно.")

    return step


def integrate_left_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Вычисляет интеграл методом левых прямоугольников."""
    step = _validate_nodes(nodes)

    # Для левых прямоугольников используем все узлы, кроме последнего.
    values = np.array(
        [function(float(x)) for x in nodes[:-1]],
        dtype=np.float64,
    )

    return float(step * np.sum(values))


def integrate_right_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Вычисляет интеграл методом правых прямоугольников."""
    step = _validate_nodes(nodes)

    # Для правых прямоугольников используем все узлы, кроме первого.
    values = np.array(
        [function(float(x)) for x in nodes[1:]],
        dtype=np.float64,
    )

    return float(step * np.sum(values))


def integrate_midpoint_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Вычисляет интеграл методом средних прямоугольников."""
    step = _validate_nodes(nodes)

    # Находим середины всех соседних пар узлов.
    midpoints = (nodes[:-1] + nodes[1:]) / 2.0

    values = np.array(
        [function(float(x)) for x in midpoints],
        dtype=np.float64,
    )

    return float(step * np.sum(values))
