"""Модуль реализаций методов прямоугольников."""

# System imports

# External imports
import numpy as np
from numpy.typing import NDArray

# User imports
from .type_aliases import Integrand

#############################################


def integrate_left_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Вычисление интеграла методом левых прямоугольников.

    L_h = h * sum_{i=0}^{n-1} f(x_i)
    """
    if len(nodes) < 2:
        raise ValueError("Число узлов должно быть не менее 2.")

    h = (nodes[-1] - nodes[0]) / (len(nodes) - 1)
    total = sum(function(float(x)) for x in nodes[:-1])
    return float(h * total)


def integrate_right_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Вычисление интеграла методом правых прямоугольников.

    R_h = h * sum_{i=1}^{n} f(x_i)
    """
    if len(nodes) < 2:
        raise ValueError("Число узлов должно быть не менее 2.")

    h = (nodes[-1] - nodes[0]) / (len(nodes) - 1)
    total = sum(function(float(x)) for x in nodes[1:])
    return float(h * total)


def integrate_midpoint_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Вычисление интеграла методом средних прямоугольников.

    M_h = h * sum_{i=0}^{n-1} f((x_i + x_{i+1}) / 2)
    """
    if len(nodes) < 2:
        raise ValueError("Число узлов должно быть не менее 2.")

    h = (nodes[-1] - nodes[0]) / (len(nodes) - 1)
    midpoints = (nodes[:-1] + nodes[1:]) / 2.0
    total = sum(function(float(m)) for m in midpoints)
    return float(h * total)
