import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand
def integrate_simpson(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    ...
