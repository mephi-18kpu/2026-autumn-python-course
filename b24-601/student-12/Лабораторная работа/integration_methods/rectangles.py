"""Методы прямоугольников для численного интегрирования."""

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
    """Метод левых прямоугольников."""
    h = nodes[1] - nodes[0]
    total_sum = 0.0
    
    # Суммируем значения функции на левых границах каждого интервала
    for i in range(len(nodes) - 1):
        total_sum = total_sum + function(nodes[i])
        
    return float(h * total_sum)


def integrate_right_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Метод правых прямоугольников."""
    h = nodes[1] - nodes[0]
    total_sum = 0.0
    
    # Суммируем значения функции на правых границах каждого интервала
    for i in range(1, len(nodes)):
        total_sum = total_sum + function(nodes[i])
        
    return float(h * total_sum)


def integrate_midpoint_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Метод средних прямоугольников."""
    h = nodes[1] - nodes[0]
    total_sum = 0.0
    
    # Вычисляем функцию в серединах интервалов
    for i in range(len(nodes) - 1):
        mid_x = (nodes[i] + nodes[i+1]) / 2.0
        total_sum = total_sum + function(mid_x)
        
    return float(h * total_sum)