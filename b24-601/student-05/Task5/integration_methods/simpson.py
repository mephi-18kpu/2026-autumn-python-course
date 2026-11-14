from typing import List
from .type_aliases import Integrand, IntegrationMethod
from numpy.typing import NDArray
import numpy as np
def integrate_simpson(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    ...
