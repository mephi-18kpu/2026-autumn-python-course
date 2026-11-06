"""Методы прямоугольников"""

import numpy as np
from numpy.typing import NDArray

from .type_aliases import Integrand


def integrate_left_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    #Интеграл методом левых прямоугольников
    if nodes.ndim != 1 or len(nodes) < 2:
        raise ValueError
    if np.any(np.diff(nodes) <= 0):
        raise ValueError

    total = 0.0

    for i in range(len(nodes) - 1):
        step = float(nodes[i + 1] - nodes[i])
        total += function(float(nodes[i])) * step

    return float(total)


def integrate_right_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    #Интеграл методом правых прямоугольников
    if nodes.ndim != 1 or len(nodes) < 2:
        raise ValueError
    if np.any(np.diff(nodes) <= 0):
        raise ValueError

    total = 0.0

    for i in range(len(nodes) - 1):
        step = float(nodes[i + 1] - nodes[i])
        total += function(float(nodes[i + 1])) * step

    return float(total)


def integrate_midpoint_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    #Итеграл методом средних прямоугольников."
    if nodes.ndim != 1 or len(nodes) < 2:
        raise ValueError
    if np.any(np.diff(nodes) <= 0):
        raise ValueError

    total = 0.0

    for i in range(len(nodes) - 1):
        step = float(nodes[i + 1] - nodes[i])
        middle = (float(nodes[i]) + float(nodes[i + 1])) / 2.0
        total += function(middle) * step

    return float(total)
