import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand

def integrate_left_rectangles(
      nodes: NDArray[np.float64],
      function: Integrand,
  ) -> float:
    integral1 = 0
    for index in range (len(nodes)-1):
        integral1 += (nodes[index+1]-nodes[index])*function(nodes[index])
    return float(integral1)

def integrate_right_rectangles(
        nodes: NDArray[np.float64],
        function: Integrand,
    ) -> float:
    integral2 = 0
    for index in range(len(nodes)-1):
        integral2 += (nodes[index + 1] - nodes[index]) * function(nodes[index+1])
    return float(integral2)

def integrate_midpoint_rectangles(
        nodes: NDArray[np.float64],
        function: Integrand,
    ) -> float:
    integral3 = 0
    for index in range(len(nodes)-1):
        integral3 += (nodes[index + 1] - nodes[index]) * function(((nodes[index + 1])+nodes[index])/2)
    return float(integral3)
