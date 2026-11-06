"""Методы прямоугольников для численного интегрирования."""
import numpy as np
from numpy.typing import NDArray
# User imports
from .type_aliases import Integrand
def integrate_left_rectangles(
        nodes: NDArray[np.float64],
        function: Integrand,
) -> float:
    """Метод левых прямоугольников.

    """
    h = nodes[1] - nodes[0]  # Шаг сетки
    # Берём значения функции во всех точках КРОМЕ последней
    y = np.array([function(x) for x in nodes[:-1]])
    return float(h * np.sum(y))
def integrate_right_rectangles(
        nodes: NDArray[np.float64],
        function: Integrand,
) -> float:
    """Метод правых прямоугольников.

    """
    h = nodes[1] - nodes[0]
    # Берём значения функции во всех точках КРОМЕ первой
    y = np.array([function(x) for x in nodes[1:]])
    return float(h * np.sum(y))
def integrate_midpoint_rectangles(
        nodes: NDArray[np.float64],
        function: Integrand,
) -> float:
    """Метод средних прямоугольников.

    """
    h = nodes[1] - nodes[0]
    # Находим середины каждого отрезка
    midpoints = (nodes[:-1] + nodes[1:]) / 2.0
    y = np.array([function(x) for x in midpoints])
    return float(h * np.sum(y))