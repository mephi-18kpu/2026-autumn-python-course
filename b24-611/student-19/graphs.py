import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 6*np.pi, 1000)
y = np.cos(x)

fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(10,4))
ax[0].plot(x, y, label="график косинуса", color="tab:blue")
ax[0].scatter(x[::10], y[::10], label="", color="tab:red")
ax[0].set_xlabel("Угол")
ax[0].set_ylabel("Значение косинуса")
ax[0].grid(True)
ax[0].legend()

x1 = np.linspace(0, 6*np.pi, 1000)
y1 = np.sin(x)


ax[1].plot(x1, y1, label="график синуса", color="tab:blue")
ax[1].scatter(x1[::10], y1[::10], label="", color="tab:red")
ax[1].set_xlabel("Угол")
ax[1].set_ylabel("Значение синуса")
ax[1].grid(True)
ax[1].legend()

x2 = np.linspace(0, 6*np.pi, 1000)
y2 = np.sinh(x)


ax[2].plot(x2, y2, label="график hсинуса", color="tab:blue")
ax[2].scatter(x2[::10], y2[::10], label="", color="tab:red")
ax[2].set_xlabel("Угол")
ax[2].set_ylabel("Значение hсинуса")
ax[2].grid(True)
ax[2].legend()

plt.show()

