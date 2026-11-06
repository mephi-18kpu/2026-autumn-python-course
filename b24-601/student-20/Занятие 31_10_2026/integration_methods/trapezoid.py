"""Методы трапеций."""


# System imports


# External imports
import numpy as np
from numpy.typing import NDArray


# User imports
from .type_aliases import Integrand, IntegrationMethod


#############################################

def integrate_trapezoid(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Реализация метода трапеций"""

    square = 0

    for index in range(1, len(nodes)-1):
        square += function(nodes[index])

    return float(nodes[1]*(function(nodes[0])/2 + square + function(nodes[-1])/2))
