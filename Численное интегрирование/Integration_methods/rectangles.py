from .type_aliases import Integrand
import numpy as np
from numpy.typing import NDArray

def integrate_left_rectangles(nodes: NDArray[np.float64],function: Integrand,) -> float:
    i = 0
    h = nodes[1]-nodes[0]
    for _ in range(len(nodes)-1):
        i += function(nodes[_])
    return h*i



def integrate_right_rectangles(nodes: NDArray[np.float64],function: Integrand,) -> float:
    i = 0
    h = nodes[1] - nodes[0]
    for j in range(1, len(nodes)):
        i += function(nodes[j])
    return h * i


def integrate_midpoint_rectangles(nodes: NDArray[np.float64],function: Integrand,) -> float:
    i = 0
    h = nodes[1] - nodes[0]
    for j in range(len(nodes) - 1):
        i += function((nodes[j]+nodes[j+1])/2)
    return h * i