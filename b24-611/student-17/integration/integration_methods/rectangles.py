import numpy as np
from numpy.typing import NDArray
from .type_integration import Integrand

def integrate_left_rectangles(
    nodes: NDArray[np.float64], function: Integrand
) -> float:
    h = nodes[1] - nodes[0]
    total = 0.0

    for i in range(len(nodes) - 1):
        x = nodes[i]
        height = function(float(x))
        area = h * height
        total = total + area
    return float(total)

def integrate_right_rectangles(
    nodes: NDArray[np.float64], function: Integrand
) -> float:
    h = nodes[1] - nodes[0]
    total = 0.0

    for i in range(len(nodes) - 1):
        x = nodes[i + 1]
        height = function(float(x))
        area = h * height
        total = total + area
    return float(total)

def integrate_midpoint_rectangles(
    nodes: NDArray[np.float64], function: Integrand
) -> float:
    h = nodes[1] - nodes[0]
    total = 0.0

    for i in range(len(nodes) - 1):
        x = (nodes[i] + nodes[i + 1]) / 2
        height = function(float(x))
        area = h * height
        total = total + area
    return float(total)
