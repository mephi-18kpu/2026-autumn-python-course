import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand


def integrate_left_rectangles(
        nodes: NDArray[np.float64],      #массив точек
        function: Integrand,
    ) -> float:
    if len(nodes) < 2:
        raise ValueError       #минимум 2 точки для вычисления

    h = nodes[1] - nodes[0]

    s = sum(function(x) for x in nodes[:-1])
    return float(h * s)

def integrate_right_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand)\
    -> float:
    if len(nodes) < 2:
        raise ValueError

    h = nodes[1] - nodes[0]

    s = sum(function(x) for x in nodes[1:])
    return float(h * s)

def integrate_midpoint_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    if len(nodes) < 2:
        raise ValueError("мин 2 узла")
    h = nodes[1] - nodes[0]
    s = sum(function((x1 + x2) / 2) for x1, x2 in zip(nodes[:-1], nodes[1:]))
    return float(h * s)
