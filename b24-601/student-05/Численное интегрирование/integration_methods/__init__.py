from typing import List

# External imports

# User imports
from .rectangles import (
    integrate_left_rectangles,
    integrate_midpoint_rectangles,
    integrate_right_rectangles,
)
from .simpson import integrate_simpson
from .trapezoid import integrate_trapezoid
from .type_aliases import Integrand, IntegrationMethod

#############################################


__all__: List[str] = [
    "Integrand",
    "IntegrationMethod",
    "integrate_left_rectangles",
    "integrate_midpoint_rectangles",
    "integrate_right_rectangles",
    "integrate_trapezoid",
    "integrate_simpson",
]
