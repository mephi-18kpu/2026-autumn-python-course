from .type_aliases import Integrand
from numpy.typing import NDArray
from numpy import float64 as np

def integrate_trapezoid(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    ...
