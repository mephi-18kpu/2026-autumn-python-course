"""Метод Симпсона (метод парабол) для численного интегрирования."""
import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand
def integrate_simpson(
        nodes: NDArray[np.float64],
        function: Integrand,
) -> float:
    """Метод Симпсона (метод парабол).

    """
    if len(nodes) < 3 or len(nodes) % 2 == 0:
        raise ValueError("Для метода Симпсона нужно нечётное число узлов (>= 3).")

    h = nodes[1] - nodes[0]
    y = np.array([function(x) for x in nodes])


    sum_odds = np.sum(y[1:-1:2])
    sum_evens = np.sum(y[2:-1:2])

    result = y[0] + 4 * sum_odds + 2 * sum_evens + y[-1]
    return float((h / 3.0) * result)