import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand


def integrate_left_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    h = nodes[1] - nodes[0]
    s = h * sum(function(node) for node in nodes[:-1])
    return s


def integrate_right_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    h = nodes[1] - nodes[0]
    s = h * sum(function(node) for node in nodes[1:])
    return s


def integrate_midpoint_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    h = nodes[1] - nodes[0]
    s = h * sum(function(node) for node in (nodes[1:] + nodes[:-1])/2 )
    return s
