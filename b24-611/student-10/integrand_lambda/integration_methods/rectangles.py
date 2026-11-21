import numpy as np
from .type_aliases import Integrand, Nodes


def integrate_left_rectangles(nodes: Nodes, function: Integrand) -> float:
    h = float(nodes[1] - nodes[0])
    total = 0.0
    for x in nodes[:-1]:            # все узлы, кроме последнего
        total += function(float(x))
    return float(total * h)


def integrate_right_rectangles(nodes: Nodes, function: Integrand) -> float:
    h = float(nodes[1] - nodes[0])
    total = 0.0
    for x in nodes[1:]:             # все узлы, кроме первого
        total += function(float(x))
    return float(total * h)


def integrate_midpoint_rectangles(nodes: Nodes, function: Integrand) -> float:
    h = float(nodes[1] - nodes[0])
    total = 0.0
    for i in range(len(nodes) - 1):
        mid = (nodes[i] + nodes[i + 1]) / 2.0
        total += function(float(mid))
    return float(total * h)
