def integrate_left_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    return float(
        np.sum(function(nodes[:-1]) * np.diff(nodes))
    )



def integrate_right_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    return float(
        np.sum(function(nodes[1:]) * np.diff(nodes))
    )



def integrate_midpoint_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    midpoints = (nodes[:-1] + nodes[1:]) / 2
    return float(
        np.sum(function(midpoints) * np.diff(nodes))
    )
