
import numpy as np
import matplotlib.pyplot as plt

t_s = np.linspace(0, 2, 2001)

# Исходные данные
k = 0.1
m = 1
g = 10
v_0 = 5

delta_t = t_s[1] - t_s[0]
alpha = np.radians(45)

vxs = []
vys = []
xs = [0]
ys = [0]

# Начальные проекции скорости
v_x = v_0 * np.cos(alpha)
v_y = v_0 * np.sin(alpha)

for i in range(len(t_s) - 1):

    v_x = v_x * (1 - k * delta_t / m)
    v_y = v_y * (1 - k * delta_t / m) - g * delta_t

    vxs.append(v_x)
    vys.append(v_y)

    xs.append(v_x * delta_t)
    ys.append(v_y * delta_t)

# Получение координат
xs = np.cumsum(np.array(xs))
ys = np.cumsum(np.array(ys))

# Оставляем точки выше поверхности земли
mask = ys >= 0

plt.plot(xs[mask], ys[mask], label="Траектория")
plt.xlabel("x, м")
plt.ylabel("y, м")
plt.title("Движение тела с сопротивлением воздуха")
plt.legend()
plt.grid()
plt.axis("equal")
plt.show()
