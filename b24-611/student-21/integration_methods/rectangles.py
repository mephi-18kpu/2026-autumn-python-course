import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand

def integrate_left_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:

    h=nodes[1] - nodes[0]
    values =[function(x) for x in nodes[:-1]]
    return float(h * sum(values))


def integrate_right_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:

    h =nodes[1] - nodes[0]
    values =[function(x) for x in nodes[1:]]
    return float(h * sum(values))


def integrate_midpoint_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:

    h =nodes[1] - nodes[0]
    total = 0
    for i in range(len(nodes)-1):
        midpoint=(nodes[i]+nodes[i+1])/2
        total +=function(midpoint)

    return float(h * total)
