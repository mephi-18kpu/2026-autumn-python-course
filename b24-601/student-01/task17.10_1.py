from math import degrees

import matplotlib.pyplot as plt
import numpy as np

angles = np.linspace(0, 1080, 180)
radians = np.deg2rad(angles)

fig, ax = plt.subplots(figsize=(12, 8.5))
ax.plot(angles, np.sin(radians)*(6*np.pi - radians), label="Синус", color="tab:red")
ax.plot(angles, np.sin(radians)*radians, label="Косинус", color="tab:blue")
ax.set_xlabel("Угол, градусы")
ax.set_ylabel("Значение функции")
ax.set_title("Интерферометр Максименко")
ax.grid(True)
ax.legend()
plt.show()




















