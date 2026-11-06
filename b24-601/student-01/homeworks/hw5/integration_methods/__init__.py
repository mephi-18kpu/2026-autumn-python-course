from typing import List

# User imports
from .rectangles import (
    integrate_left_rectangles,
    integrate_midpoint_rectangles,
    integrate_right_rectangles,
)
from homeworks.hw5.integration_methods.simpson import integrate_simpson
from homeworks.hw5.integration_methods.trapezoid import integrate_trapezoid
from .type_aliases import Integrand, IntegrationMethod


__all__: List[str] = [
    "Integrand",
    "IntegrationMethod",
    "integrate_left_rectangles",
    "integrate_midpoint_rectangles",
    "integrate_right_rectangles",
    "integrate_trapezoid",
    "integrate_simpson",
]
