"""Модуль, содержащий алгоритмы методов прямоугольников."""

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
    """Вычисление интеграла методом левых прямоугольников."""
    
    step_size = nodes[1] - nodes[0]
    accumulator = 0.0
    
    for index in range(len(nodes) - 1):
        accumulator += function(nodes[index])
        
    return float(step_size * accumulator)


def integrate_right_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Вычисление интеграла методом правых прямоугольников."""
    
    step_size = nodes[1] - nodes[0]
    accumulator = 0.0
    
    for index in range(1, len(nodes)):
        accumulator += function(nodes[index])
        
    return float(step_size * accumulator)


def integrate_midpoint_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Вычисление интеграла методом средних прямоугольников."""
    
    step_size = nodes[1] - nodes[0]
    accumulator = 0.0
    
    for index in range(len(nodes) - 1):
        midpoint_coordinate = (nodes[index] + nodes[index + 1]) / 2.0
        accumulator += function(midpoint_coordinate)
        
    return float(step_size * accumulator)