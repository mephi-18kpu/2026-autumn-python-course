"""Метод Симпсона."""


# System imports


# External imports
import numpy as np
from numpy.typing import NDArray


# User imports
from .type_aliases import Integrand, IntegrationMethod


#############################################

def integrate_simpson(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Реализация метода Симпсона."""

    square = 0

    for index in range(1, int(len(nodes) - 1)):
        coef = 4 if index % 2 == 1 else 2
        square += coef * function(nodes[index])

    return float((nodes[1]/3)*(function(nodes[0]) + square + function(nodes[-1])))
