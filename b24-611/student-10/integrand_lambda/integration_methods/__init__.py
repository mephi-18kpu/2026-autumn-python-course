from typing import List
from integration_methods.rectangles import (
    integrate_left_rectangles,
    integrate_midpoint_rectangles,
    integrate_right_rectangles,
)
from integration_methods.trapezoid import integrate_trapezoid
from integration_methods.simpson import integrate_simpson
from integration_methods.type_aliases import Integrand, IntegrationMethod

__all__: List[str] = [
    "Integrand",
    "IntegrationMethod",
    "integrate_left_rectangles",
    "integrate_midpoint_rectangles",
    "integrate_right_rectangles",
    "integrate_trapezoid",
    "integrate_simpson",
]
