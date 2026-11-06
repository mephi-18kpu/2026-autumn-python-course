"""Модуль, реализующий метод трапеций."""

# System imports

# External imports
import numpy as np
from numpy.typing import NDArray

# User imports
from .type_aliases import Integrand

#############################################


def integrate_trapezoid(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Вычисление интеграла составным методом трапеций."""
    
    step_size = nodes[1] - nodes[0]
    accumulator = 0.0
    
    # Учёт краевых точек с половинным весом
    accumulator += 0.5 * function(nodes[0])
    accumulator += 0.5 * function(nodes[-1])
    
    # Учёт внутренних узлов сетки
    for index in range(1, len(nodes) - 1):
        accumulator += function(nodes[index])
        
    return float(step_size * accumulator)