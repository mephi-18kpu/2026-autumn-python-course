"""Методы левых, правых и средних прямоугольников."""

# System imports

# External imports
import numpy as np
from numpy.typing import NDArray

# User imports
from .type_aliases import Integrand

#############################################


def _validate_nodes(nodes: NDArray[np.float64], minimum_size: int = 2) -> float:
    """Проверить равномерность и возрастание сетки и вернуть её шаг."""
    if nodes.ndim != 1:
        raise ValueError("Массив узлов должен быть одномерным.")
    if nodes.size < minimum_size:
        raise ValueError(f"Нужно не менее {minimum_size} узлов.")

    differences = np.diff(nodes)
    if np.any(differences <= 0):
        raise ValueError("Узлы должны строго возрастать.")

    step = float(differences[0])
    if not np.allclose(differences, step):
        raise ValueError("Сетка должна быть равномерной.")

    return step


def integrate_left_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Вычислить интеграл методом левых прямоугольников."""
    step = _validate_nodes(nodes)
    values = [function(float(node)) for node in nodes[:-1]]
    return float(step * sum(values))


def integrate_right_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Вычислить интеграл методом правых прямоугольников."""
    step = _validate_nodes(nodes)
    values = [function(float(node)) for node in nodes[1:]]
    return float(step * sum(values))


def integrate_midpoint_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Вычислить интеграл методом средних прямоугольников."""
    step = _validate_nodes(nodes)
    midpoints = (nodes[:-1] + nodes[1:]) / 2.0
    values = [function(float(point)) for point in midpoints]
    return float(step * sum(values))
