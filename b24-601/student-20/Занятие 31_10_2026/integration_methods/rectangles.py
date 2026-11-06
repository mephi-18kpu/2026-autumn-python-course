"""Методы прямоугольников."""

# System imports


# External imports
import numpy as np
from numpy.typing import NDArray


# User imports
from .type_aliases import Integrand, IntegrationMethod


#############################################

def integrate_left_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Реализация метода левых прямоугольников."""

    square = 0

    for index in range(len(nodes)-1):
        square += function(nodes[index])

    return float(nodes[1] * square)


def integrate_right_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Реализация метода правых прямоугольников."""

    square = 0

    for index in range(1, len(nodes)):
        square += function(nodes[index])

    return float(nodes[1] * square)


def integrate_midpoint_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Реализация метода средних прямоугольников."""

    square = 0

    for index in range(len(nodes) - 1):
        square += function((nodes[index] + nodes[index + 1]) / 2)

    return float(nodes[1] * square)
