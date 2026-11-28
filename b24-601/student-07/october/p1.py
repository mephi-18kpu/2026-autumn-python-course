import numpy as np
from numpy.typing import NDArray

def integrate_left_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    if len(nodes) < 2:
        raise ValueError("Для метода прямоугольников нужно хотя бы два узла.")

    h = nodes[1] - nodes[0]

    integral_sum = sum(function(x) for x in nodes[:-1])

    return float(h * integral_sum)
