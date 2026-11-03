import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand

def integrate_simpson(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    if len(nodes) % 2 == 0:
        raise ValueError("для метода Cимпсона нужно нечетное число узлов")

    h = nodes[1] - nodes[0]
    total = function(nodes[0]) + function(nodes[-1])
    for i in range(1, len(nodes)-1):
        if i % 2 != 0:
            total += 4*function(nodes[i])
        else:
            total += 2*function(nodes[i])

    return float((h/3) * total)
