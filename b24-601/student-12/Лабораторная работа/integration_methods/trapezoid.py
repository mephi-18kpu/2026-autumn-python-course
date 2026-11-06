"""Метод трапеций для численного интегрирования."""

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
    """Метод трапеций."""
    h = nodes[1] - nodes[0]
    total_sum = 0.0
    
    # Крайние узлы входят в формулу с коэффициентом 1/2
    total_sum = total_sum + function(nodes[0]) / 2.0
    total_sum = total_sum + function(nodes[-1]) / 2.0
    
    # Внутренние узлы суммируются с коэффициентом 1
    for i in range(1, len(nodes) - 1):
        total_sum = total_sum + function(nodes[i])
        
    return float(h * total_sum)