import numpy as np

def integrate_left_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    h = nodes[1]-nodes[0]
    integral=h*np.sum(function(nodes[:-1]))
    return float(integral)



def integrate_right_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    h = nodes[1] - nodes[0]
    integral = h * np.sum(function(nodes[1:]))
    return float(integral)


def integrate_midpoint_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    h = nodes[1]-nodes[0]
    midpoints = (nodes[:-1] + nodes[1:]) / 2.0
    integral = h * np.sum(function(midpoints))
    return float(integral)
