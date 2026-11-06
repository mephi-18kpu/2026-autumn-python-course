from typing import List
import numpy as np

from numpy.typing import NDArray

from .type_aliases import Integrand

__all__: List[str] = [
    "integrate_left_rectangles",
    "integrate_right_rectangles",
    "integrate_midpoint_rectangles",
]

def integrate_left_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    h = nodes[1] - nodes[0]
    return float(h * np.sum(function(nodes[:-1]))) #суммируем все кроме последнего,так как суммируем все левые - то есть до n-1

def integrate_right_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    h = nodes[1] - nodes[0]
    return float(h * np.sum(function(nodes[1:]))) #от первого не вкл

def integrate_midpoint_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    h = nodes[1] - nodes[0]
    middle_p = nodes[:-1] + h/2 #была самая левая точка сдвинули ее на полклетки
    return float(h * np.sum(function(middle_p)))
