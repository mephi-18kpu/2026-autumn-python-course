from cProfile import label

import numpy as np
import matplotlib.pyplot as plt
angles = np.linspace(0, 180*6, 180*6+1)
radians = np.deg2rad(angles)
fig, ax = plt.subplots(figsize=(8, 4))
plt.plot(angles, np.sin(radians), label='Синус', color='blue', linestyle = ':')
plt.plot(angles, np.cos(radians), label='Косинус', color='blue')
ax.set_xlabel("Угол, градусы")
ax.set_ylabel("Значение функции")
ax.set_title("Синус и косинус")
ax.grid(True)
ax.legend()
plt.show()
