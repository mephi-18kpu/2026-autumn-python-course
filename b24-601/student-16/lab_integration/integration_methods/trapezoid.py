"""Метод трапеций для численного интегрирования."""
# System imports
# External imports
import numpy as np
from numpy.typing import NDArray
# User imports
from .type_aliases import Integrand
def integrate_trapezoid(
        nodes: NDArray[np.float64],
        function: Integrand,
) -> float:
    """Метод трапеций.

    """
    h = nodes[1] - nodes[0]
    y = np.array([function(x) for x in nodes])
    # Формула трапеций: крайние точки с весом 1/2, внутренние с весом 1
    result = 0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1]
    return float(h * result)