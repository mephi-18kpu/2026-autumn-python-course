import numpy as np
from numpy.typing import NDArray

from .type_aliases import Integrand


def integrate_trapezoid(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Метод трапеций."""
    if len(nodes) < 2:
        raise ValueError("Для метода трапеций нужно хотя бы 2 узла.")

    h = nodes[1] - nodes[0]
    total = 0.5 * function(float(nodes[0])) + 0.5 * function(float(nodes[-1]))
    for i in range(1, len(nodes) - 1):
        total += function(float(nodes[i]))
    return float(h * total)
