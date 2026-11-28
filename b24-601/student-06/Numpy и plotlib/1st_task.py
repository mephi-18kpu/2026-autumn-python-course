import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2 * np.pi, 100)  # Углы от 0 до 2π
r = 1 + np.sin(theta)**4  # Радиус как функция угла

plt.polar(theta, r)
plt.title("Пример полярного графика")
plt.show()
