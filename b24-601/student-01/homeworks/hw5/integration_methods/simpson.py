import math


import numpy as np
from numpy.typing import NDArray


from .type_aliases import Integrand


def integrate_simpson(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:

    if nodes.ndim != 1 or nodes.size < 3 or nodes.size % 2 == 0:
        # Сообщение об ошибке вывести то какое-то надо
        raise ValueError(
        )

    h = float(nodes[-1] - nodes[0]) / (nodes.size - 1)
    values = [function(float(x)) for x in nodes]
    odd = math.fsum(values[1:-1:2])
    even = math.fsum(values[2:-1:2])
    return h / 3.0 * (values[0] + 4.0 * odd + 2.0 * even + values[-1])
