"""Методы прямоугольников."""

from typing import cast
import numpy as np
from numpy.typing import NDArray

from .type_aliases import Integrand


def integrate_left_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Метод левых прямоугольников."""
    if len(nodes) < 2:
        raise ValueError("Для метода прямоугольников нужно хотя бы 2 узла.")

    h = nodes[1] - nodes[0]
    total = sum(function(float(x)) for x in nodes[:-1])
    return float(h * total)


def integrate_right_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Метод правых прямоугольников."""
    if len(nodes) < 2:
        raise ValueError("Для метода прямоугольников нужно хотя бы 2 узла.")

    h = nodes[1] - nodes[0]
    total = sum(function(float(x)) for x in nodes[1:])
    return float(h * total)


def integrate_midpoint_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Метод средних прямоугольников."""
    if len(nodes) < 2:
        raise ValueError("Для метода прямоугольников нужно хотя бы 2 узла.")

    h = nodes[1] - nodes[0]
    total = 0.0
    for i in range(len(nodes) - 1):
        mid = (nodes[i] + nodes[i + 1]) / 2.0
        total += function(float(mid))
    return float(h * total)
