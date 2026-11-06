"""Метод Симпсона для численного интегрирования."""

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
    """Метод Симпсона."""
    h = nodes[1] - nodes[0]
    total_sum = 0.0
    
    # Крайние узлы входят с коэффициентом 1
    total_sum = total_sum + function(nodes[0])
    total_sum = total_sum + function(nodes[-1])
    
    # Внутренние узлы чередуют веса 4 и 2
    for i in range(1, len(nodes) - 1):
        if i % 2 == 1:
            # Узлы с нечетными индексами умножаются на 4
            total_sum = total_sum + 4 * function(nodes[i])
        else:
            # Узлы с четными индексами умножаются на 2
            total_sum = total_sum + 2 * function(nodes[i])
            
    return float((h / 3.0) * total_sum)