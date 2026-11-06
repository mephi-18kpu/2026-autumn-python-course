import numpy as np
from numpy.typing import NDArray

from .type_aliases import Integrand

def integrate_simpson(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    count_nodes = nodes.size
    if count_nodes<3:
        raise ValueError("Метод Симпсона требует не менее трех узлов")
    if (count_nodes-1)%2==1:
        raise ValueError("Метод Симпсона требует четного числа интервалов")
    h = float(nodes[1] - nodes[0])
    values = function(nodes)
    return (h / 3.0) * (values[0] + 4.0 * np.sum(values[1:-1:2]) + 2.0 * np.sum(values[2:-1:2]) + values[-1])


