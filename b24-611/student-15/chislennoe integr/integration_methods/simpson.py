import numpy as np
from numpy.typing import NDArray

from .type_aliases import Integrand


def integrate_simpson(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Метод Симпсона."""
    if len(nodes) < 3 or len(nodes) % 2 == 0:
        raise ValueError("Для метода Симпсона нужно нечётное число узлов (не меньше 3).")

    h = nodes[1] - nodes[0]
    total = function(float(nodes[0])) + function(float(nodes[-1]))

    for i in range(1, len(nodes) - 1, 2):
        total += 4.0 * function(float(nodes[i]))
    for i in range(2, len(nodes) - 1, 2):
        total += 2.0 * function(float(nodes[i]))

    return float((h / 3.0) * total)
