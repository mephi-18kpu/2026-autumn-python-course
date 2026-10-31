"""."""

# System imports


# External imports
import numpy as np
from numpy.typing import NDArray


# User imports
from type_aliases import Integrand, IntegrationMethod


#############################################

def integrate_left_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:

    return None


def integrate_right_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    pass


def integrate_midpoint_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    pass
