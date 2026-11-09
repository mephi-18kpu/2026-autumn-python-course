import numpy as np

def integrate_trapezoid(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    # Тут тоже со срезами молодец
    h = nodes[1] - nodes[0]
    integral = h*0.5* np.sum(function(nodes[:-1]) + function(nodes[1:]))

    return float(integral)
