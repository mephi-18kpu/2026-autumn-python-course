import numpy as np
from numpy.typing import NDArray

from .type_aliases import Integrand



def proverka_nodes(nodes: NDArray[np.float64]) -> float:

    if nodes.ndim != 1:
        raise ValueError("Массив узлов не одномерный.")
    if nodes.size < 2:
        raise ValueError("Нужны хотя бы два узла.")

    differences = np.diff(nodes)
    if np.any(differences <= 0):
        raise ValueError("Сетка - не строго возрастающая.")
    if not np.allclose(differences, differences[0]):
        raise ValueError("Сетка - не равномерна.")

    return float(differences[0])


def integrate_left_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:

    h = proverka_nodes(nodes)
    result = h * sum(function(float(x)) for x in nodes[:-1])
    return float(result)


def integrate_right_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:

    h = proverka_nodes(nodes)
    result = h * sum(function(float(x)) for x in nodes[1:])
    return float(result)


def integrate_midpoint_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:

    h = proverka_nodes(nodes)
    midpoints = (nodes[:-1] + nodes[1:]) / 2.0
    result = h * sum(function(float(x)) for x in midpoints)
    return float(result)
