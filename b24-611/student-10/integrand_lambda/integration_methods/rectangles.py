import numpy as np
from numpy.typing import NDArray
from integration_methods.type_aliases import Integrand

def integrate_left_rectangles(nodes: NDArray[np.float64], function: Integrand) -> float:
    h = float(nodes[1] - nodes[0])
    f_values = function(nodes[:-1])
    return float(np.sum(f_values) * h)

def integrate_right_rectangles(nodes: NDArray[np.float64], function: Integrand) -> float:
    h = float(nodes[1] - nodes[0])
    f_values = function(nodes[1:])
    return float(np.sum(f_values) * h)

def integrate_midpoint_rectangles(nodes: NDArray[np.float64], function: Integrand) -> float:
    h = float(nodes[1] - nodes[0])
    mid_points = nodes[:-1] + h / 2.0
    f_values = function(mid_points)
    return float(np.sum(f_values) * h)
