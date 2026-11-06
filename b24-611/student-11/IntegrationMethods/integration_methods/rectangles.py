def integrate_left_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    n = len(nodes) - 1
    h = (nodes[-1] - nodes[0]) / n
    result = 0.0
    for i in range(n): # Берём левые вершины прямоугольников
        result += function(float(nodes[i]))
    return float(result * h)


def integrate_right_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    n = len(nodes) - 1
    h = (nodes[-1] - nodes[0]) / n
    result = 0.0
    for i in range(0, n+1): # Берём правые вершины прямоугольников
        result += function(float(nodes[i]))
    return float(result * h)


def integrate_midpoint_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    n = len(nodes) - 1
    h = (nodes[-1] - nodes[0]) / n
    result = 0.0
    for i in range(n):
        centre = (nodes[i] + nodes[i+1]) / 2
        result += function(float(centre))
    return float(result * h)
