import numpy as np
from numpy.typing import NDArray

from .type_aliases import Integrand



def integrate_trapezoid(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:

    if nodes.ndim != 1:
        raise ValueError("Массив узлов - одномерный.")
    if nodes.size < 2:
        raise ValueError("Нужны хотя бы два узла.")

    differences = np.diff(nodes)
    if np.any(differences <= 0):
        raise ValueError("Сетка - не строго возрастающая.")
    if not np.allclose(differences, differences[0]):
        raise ValueError("Сетка - не равномерна.")

    h = float(differences[0])
    values = [function(float(x)) for x in nodes]
    result = h * (
        values[0] / 2.0
        + sum(values[1:-1])
        + values[-1] / 2.0
    )
    return float(result)
