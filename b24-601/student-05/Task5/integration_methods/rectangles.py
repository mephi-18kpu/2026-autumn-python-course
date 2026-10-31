from typing import List
from .type_aliases import Integrand, IntegrationMethod
from numpy.typing import NDArray
import numpy as np
def integrate_left_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    ans = 0
    h = nodes[1]-nodes[0]
    for i in range(nodes.size):
        ans+=function(nodes[i])
    ans*=h
    return ans


def integrate_right_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    ans = 0
    h = nodes[1] - nodes[0]
    for i in range(nodes.size-1):
        ans += function(nodes[i+1])
    ans *= h
    return ans


def integrate_midpoint_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    ...
