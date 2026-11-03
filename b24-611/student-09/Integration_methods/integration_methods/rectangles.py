# System imports

# External imports
from .type_alliases import *

# User imports

#############################################

def integrate_left_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    res=0
    for i in range(0, len(nodes)-1) :
        res+=function(nodes[i])*(nodes[i+1]-nodes[i])
    return res

def integrate_right_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    res=0
    for i in range(1, len(nodes)):
        res += function(nodes[i])*(nodes[i]-nodes[i-1])
    return res


def integrate_midpoint_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    res=0
    for i in range(0, len(nodes)-1):
        res += function((nodes[i+1]+nodes[i])/2)*(nodes[i+1]-nodes[i])
    return res
