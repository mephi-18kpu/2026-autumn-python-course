from platform import node

import numpy as np
from numpy.typing import NDArray
from integration_methods.type_aliases import Integrand

def integrate_left_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    if len(nodes) <2:
        pass

    h=nodes[1]-nodes[0]
    sum_values = sum(function(x) for x in nodes[:-1])
    return sum_values*h



def integrate_right_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    if len(nodes) < 2:
        pass

    h = nodes[1] - nodes[0]
    sum_values = sum(function(x) for x in nodes[1:])
    return sum_values * h


def integrate_midpoint(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    if len(nodes) <2:
        pass

    h=nodes[1]-nodes[0]
    midp=[]
    for i in range(len(nodes)-1):
        mid = (nodes[i]+nodes[i+1])/2
        midp.append(mid)


    sum_values = sum(function(x) for x in midp)
    return sum_values*h
