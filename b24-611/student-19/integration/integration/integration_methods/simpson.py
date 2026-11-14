import numpy as np
from numpy.typing import NDArray

from .type_aliases import Integrand



def integrate_simpson(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    if nodes.ndim != 1:
        raise ValueError("Массив узлов - одномерный.")
    if nodes.size < 3:
        raise ValueError("Нужно хотя бы три узла.")
    if nodes.size % 2 == 0:
        raise ValueError("Требуется нечётное число узлов.")

    differences = np.diff(nodes)
    if np.any(differences <= 0):
        raise ValueError("Сетка - не строго возрастающая.")
    if not np.allclose(differences, differences[0]):
        raise ValueError("Сетка - не равномерна.")

    h = float(differences[0])
    values = [function(float(x)) for x in nodes]

    odd_sum = sum(values[1:-1:2])
    even_sum = sum(values[2:-1:2])
    result = (h / 3.0) * (
        values[0] + 4.0 * odd_sum + 2.0 * even_sum + values[-1]
    )
    return float(result)
