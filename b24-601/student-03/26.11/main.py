import numpy as np
import matplotlib.pyplot as plt


v0    = 50.0
alpha = 45.0
g     = 9.81
k     = 0.01
dt    = 0.001
t_max = 30.0



alpha_rad = np.deg2rad(alpha)
vx0 = v0 * np.cos(alpha_rad)
vy0 = v0 * np.sin(alpha_rad)



N_max = int(t_max / dt) + 1

t  = np.zeros(N_max)
x  = np.zeros(N_max)
y  = np.zeros(N_max)
vx = np.zeros(N_max)
vy = np.zeros(N_max)
ax = np.zeros(N_max)
ay = np.zeros(N_max)


t[0]  = 0.0
x[0]  = 0.0
y[0]  = 0.0
vx[0] = vx0
vy[0] = vy0
ax[0] = -k * vx[0]
ay[0] = -g - k * vy[0]


i = 0
while i < N_max - 1:
    vx[i+1] = vx[i] + dt * (-k * vx[i])
    vy[i+1] = vy[i] + dt * (-g - k * vy[i])

    x[i+1] = x[i] + dt * vx[i]
    y[i+1] = y[i] + dt * vy[i]

    t[i+1] = t[i] + dt

    ax[i+1] = -k * vx[i+1]
    ay[i+1] = -g - k * vy[i+1]

    if y[i+1] < 0.0:
        i += 1
        break
    i += 1

n = i + 1
t, x, y, vx, vy, ax, ay = (arr[:n] for arr in (t, x, y, vx, vy, ax, ay))


v   = np.sqrt(vx**2 + vy**2)          # модуль скорости
a   = np.sqrt(ax**2 + ay**2)          # модуль ускорения



print(f"Начальная скорость : {v0:.3f} м/с")
print(f"Угол к горизонту   : {alpha:.3f}°")
print(f"Коэф. сопротивления k = {k} 1/с")
print(f"Шаг дискретизации Δt = {dt} с")
print(f"Время полёта       : {t[-1]:.4f} с")
print(f"Дальность полёта   : {x[-1]:.4f} м")
print(f"Максимальная высота: {y.max():.4f} м")
print(f"Скорость в конце   : {v[-1]:.4f} м/с")
print(f"Угол падения       : {np.rad2deg(np.arctan2(vy[-1], vx[-1])):.3f}°")


fig, axs = plt.subplots(2, 2, figsize=(12, 9))

# 1) y(x)
axs[0, 0].plot(x, y, 'b-', lw=2)
axs[0, 0].set_xlabel('x, м')
axs[0, 0].set_ylabel('y, м')
axs[0, 0].set_title('Траектория y(x)')
axs[0, 0].grid(True, alpha = 0.4)

# 2) x(t) и y(t)
axs[0, 1].plot(t, x, 'g-', label='x(t)')
axs[0, 1].plot(t, y, 'r-', label='y(t)')
axs[0, 1].set_xlabel('t, с')
axs[0, 1].set_ylabel('координата, м')
axs[0, 1].set_title('Зависимости x(t) и y(t)')
axs[0, 1].legend()
axs[0, 1].grid(True, alpha = 0.4)

# 3) Компоненты скорости и модуль
axs[1, 0].plot(t, vx, label='vx(t)')
axs[1, 0].plot(t, vy, label='vy(t)')
axs[1, 0].plot(t, v,  'k--', label='|v(t)|')
axs[1, 0].set_xlabel('t, с')
axs[1, 0].set_ylabel('скорость, м/с')
axs[1, 0].set_title('Скорости')
axs[1, 0].legend()
axs[1, 0].grid(True, alpha = 0.4)

# 4) Компоненты ускорения и модуль
axs[1, 1].plot(t, ax, label='ax(t)')
axs[1, 1].plot(t, ay, label='ay(t)')
axs[1, 1].plot(t, a,  'k--', label='|a(t)|')
axs[1, 1].set_xlabel('t, с')
axs[1, 1].set_ylabel('ускорение, м/с²')
axs[1, 1].set_title('Ускорения')
axs[1, 1].legend()
axs[1, 1].grid(True, alpha = 0.4)

plt.tight_layout()
plt.show()
