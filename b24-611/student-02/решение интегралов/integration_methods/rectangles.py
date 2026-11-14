import numpy as np
from numpty.typing import NDArray

from .type_aliases import Integrand


def integrate_left_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand
)
