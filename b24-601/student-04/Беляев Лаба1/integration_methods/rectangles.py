import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand

def integrate_left_rectangles(nodes: NDArray[np.float64], function: Integrand) -> float:
    """Метод левых прямоугольников."""
    h = nodes[1] - nodes[0]
    return float(h * np.sum([function(x) for x in nodes[:-1]]))

def integrate_right_rectangles(nodes: NDArray[np.float64], function: Integrand) -> float:
    """Метод правых прямоугольников."""
    h = nodes[1] - nodes[0]
    return float(h * np.sum([function(x) for x in nodes[1:]]))

def integrate_midpoint_rectangles(nodes: NDArray[np.float64], function: Integrand) -> float:
    """Метод средних прямоугольников."""
    h = nodes[1] - nodes[0]
    midpoints = (nodes[:-1] + nodes[1:]) / 2.0
    return float(h * np.sum([function(m) for m in midpoints]))
