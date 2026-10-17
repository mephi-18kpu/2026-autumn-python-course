
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 6 * np.pi, 1000)
x_deg = x * 180 / np.pi
y = np.sin(x)

plt.plot(x_deg, y, color='blue', label='sin(x)')
plt.title('График синуса на три периода')
plt.xlabel('Угол (градусы)')
plt.ylabel('Значение синуса')
plt.legend()
plt.grid(True)
plt.show()
