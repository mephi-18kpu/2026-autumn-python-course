import numpy as np
from numpy.typing import NDArray

from .type_aliases import Integrand

def integrate_simpson(
    nodes: NDArray[np.float64],
    func: Integrand,
) -> float:
    if len(nodes) < 3 or len(nodes) % 2 == 0:
        raise ValueError("Нужно нечётное число узлов не меньше трёх")

    total = 0.0
    index = 0
    while index < len(nodes) - 2:
        width = nodes[index + 1] - nodes[index]
        left = func(nodes[index])
        middle = func(nodes[index + 1])
        right = func(nodes[index + 2])
        total += width / 3 * (left + 4 * middle + right)
        index += 2
    return total
