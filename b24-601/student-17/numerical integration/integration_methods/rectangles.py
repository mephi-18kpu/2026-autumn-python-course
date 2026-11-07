import numpy as np
from .type_aliases import Integrand

def integrate_left_rectangles(nodes, function: Integrand) -> float:
    """Метод левых прямоугольников."""
    h = float(nodes[1] - nodes[0])
    total = sum(function(float(x)) for x in nodes[:-1])
    return h * total


def integrate_right_rectangles(nodes, function: Integrand) -> float:
    """Метод правых прямоугольников."""
    h = float(nodes[1] - nodes[0])
    total = sum(function(float(x)) for x in nodes[1:])
    return h * total


def integrate_midpoint_rectangles(nodes, function: Integrand) -> float:
    """Метод средних прямоугольников."""
    h = float(nodes[1] - nodes[0])
    total = 0.0
    for i in range(nodes.size - 1):
        mid = (float(nodes[i]) + float(nodes[i + 1])) / 2.0
        total += function(mid)
    return h * total