"""Модуль, реализующий метод Симпсона (метод парабол)."""

# System imports

# External imports
import numpy as np
from numpy.typing import NDArray

# User imports
from .type_aliases import Integrand

#############################################


def integrate_simpson(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Вычисление интеграла составным методом Симпсона."""
    
    step_size = nodes[1] - nodes[0]
    accumulator = 0.0
    
    # Добавление значений на границах отрезка
    accumulator += function(nodes[0]) + function(nodes[-1])
    
    # Цикл по внутренним узлам с чередованием весов (4 для нечётных, 2 для чётных)
    for index in range(1, len(nodes) - 1):
        if index % 2 != 0:
            accumulator += 4.0 * function(nodes[index])
        else:
            accumulator += 2.0 * function(nodes[index])
            
    return float((step_size / 3.0) * accumulator)