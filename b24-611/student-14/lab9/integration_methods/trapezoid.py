def integrate_trapezoid(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    h = np.diff(nodes)
    left = function(nodes[:-1])
    right = function(nodes[1:])

    return float(
        np.sum((left + right) * h / 2)
    )
