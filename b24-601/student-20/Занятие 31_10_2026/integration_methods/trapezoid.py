"""."""


# System imports


# External imports
import numpy as np
from numpy.typing import NDArray


# User imports
from type_aliases import Integrand, IntegrationMethod


#############################################

def integrate_trapezoid(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    pass
