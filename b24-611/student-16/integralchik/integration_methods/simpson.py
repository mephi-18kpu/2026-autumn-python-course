import numpy as np
from numpy.typing import NDArray

from .type_aliases import Integrand

def integrate_simpson(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    h = nodes[1] - nodes[0]

    func_val = function(nodes)
    even_index = np.sum(func_val[2:-1:2]) #начинаем с индекса 2 вкл
    odd_index = np.sum(func_val[1:-1:2])#начинаем с индекса 1 вкл, так как 1 в начале озгачает 0 индекс пропускаем

    total = func_val[0] + func_val[-1] + 4*odd_index + 2*even_index

    return float((h/3.0) * total)
