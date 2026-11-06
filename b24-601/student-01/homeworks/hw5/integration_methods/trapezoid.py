import math


import numpy as np
from numpy.typing import NDArray


from .type_aliases import Integrand


def integrate_trapezoid(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    if nodes.ndim != 1 or nodes.size < 2:
        raise ValueError("Нужен одномерный массив минимум из двух узлов.")

    h = float(nodes[-1] - nodes[0]) / (nodes.size - 1)
    values = [function(float(x)) for x in nodes]
    inner = math.fsum(values[1:-1])
    return h * (values[0] / 2.0 + inner + values[-1] / 2.0)
