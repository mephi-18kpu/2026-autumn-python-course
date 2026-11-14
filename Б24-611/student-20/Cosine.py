from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

angles=np.linspace(0, 180*6, 180*6+1)
radians= np.deg2rad(angles)

fig, ax = plt.subplots(figsize=(48, 4))
ax.plot(angles, np.cos(radians), label="Косинус", color="tab:green")
ax.set_xlabel("Угол градусы")
ax.set_ylabel("Значение функции")
ax.set_title("Косинус")
ax.grid(True)
ax.legend()

plt.show()
