import numpy as np
import matplotlib.pyplot as plt


values = np.linspace(0, 1080, 36)
values_rad = np.deg2rad(values)
sin_values = np.sin(values_rad)
print(values, sin_values)


fig, ax = plt.subplots(figsize=(16,9))
ax.plot(values_rad, sin_values, label="шаыртг", color="tab:red")
ax.grid(True)

plt.show()
