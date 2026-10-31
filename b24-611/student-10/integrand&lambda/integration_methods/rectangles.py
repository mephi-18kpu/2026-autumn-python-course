import  numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand
def integrate_left_rectangle(nodes: NDArray[np.float64], function: Integrand) -> float:
    h = float(nodes[1] - nodes[0])
    f_values = np.array([function(x) for x in nodes[:-1]], dtype=np.float64)
    return float(np.sum(f_values)*h)

def integrate_right_rectangle(nodes: NDArray[np.float64], function: Integrand) -> float:
    h = float(nodes[1] - nodes[0])
    f_values = np.array([function(x) for x in nodes[1:]], dtype=np.float64)
    return float(np.sum(f_values)*h)

def integrate_mid_rectangles(nodes: NDArray[np.float64], function: Integrand) -> float:
    h = float(nodes[1] - nodes[0])
    mid = nodes[:-1] + h/2.0
    f_values = np.array([function(x) for x in mid], dtype=np.float64)
    return  float(np.sum(f_values)*h)
