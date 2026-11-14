from typing import Callable

import numpy as np

import integration_methods
from integration_methods import *

f: Integrand = lambda x: np.exp(x)
nodes1 = np.linspace(0,1, 3)
nodes2 = np.linspace(0,1, 30)
nodes3 = np.linspace(0,1, 300)
print(integration_methods.integrate_left_rectangles(nodes1, f))
print(integration_methods.integrate_left_rectangles(nodes2, f))
print(integration_methods.integrate_left_rectangles(nodes3, f))
print(integration_methods.integrate_right_rectangles(nodes1, f))
print(integration_methods.integrate_right_rectangles(nodes2, f))
print(integration_methods.integrate_right_rectangles(nodes3, f))
