import math
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Dict

from integration_methods import(
    Integrand,
    IntegrationMethod,
    integrate_left_rectangles,
    integrate_midpoint_rectangles,
    integrate_right_rectangles,
    integrate_simpson,
    integrate_trapezoid,
)

def main():
    f: Integrand = lambda x: math.exp(x)
    exact_integral: float = math.e - 1.0
    methods: Dict[str, IntegrationMethod] = {
        "Левые прямоугольники": integrate_left_rectangles,
        "Правые прямоугольники": integrate_right_rectangles,
        "Средние прямоугольники": integrate_midpoint_rectangles,
        "Симпсон": integrate_simpson,
        "Трапеция": integrate_trapezoid,
    }
    N_values: List[int] = [3, 5, 9, 17, 33, 65]
