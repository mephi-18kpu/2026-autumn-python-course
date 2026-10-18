import matplotlib.pyplot as plt
import numpy as np

# ============================================================
# ИСХОДНЫЕ ЭКСПЕРИМЕНТАЛЬНЫЕ ДАННЫЕ
# ============================================================

theta = np.array([25, 30, 35, 40, 45, 50, 55, 60])
N1 = np.array([2224, 1081, 582, 357, 212, 149, 112, 90])
N2 = 51

# ============================================================
# ВЫЧИСЛЕНИЯ ПО ФОРМУЛАМ
# ============================================================

delta_N = N1 - N2

# y = Delta_N * sin^4(theta / 2)
theta_rad = np.radians(theta)
sin4_half_theta = np.sin(theta_rad / 2) ** 4
y = delta_N * sin4_half_theta

# Относительная и абсолютная погрешности
epsilon_y = 3 * np.sqrt(N1 + N2) / (N1 - N2)
delta_y = y * epsilon_y

# ============================================================
# РАСЧЕТ КОНСТАНТЫ (СРЕДНЕГО ВЗВЕШЕННОГО)
# ============================================================

weights = 1.0 / (delta_y**2)
y_const = np.sum(weights * y) / np.sum(weights)

# ============================================================
# ГРАФИК
# ============================================================

fig, ax = plt.subplots(figsize=(12, 8.5))

# Прямая константы y = const
line = ax.axhline(
    y=y_const,
    color='tab:blue',
    linestyle='-',
    linewidth=2,
    label=rf'Теоретическая зависимость ($\Delta N \sin^4(\theta/2) = {y_const:.2f}$)',
)

# Экспериментальные точки с погрешностями
ax.errorbar(
    theta,
    y,
    yerr=delta_y,
    fmt='o',
    color=line.get_color(),
    ecolor=line.get_color(),
    markersize=5,
    capsize=4,
)

ax.axhline(0, color='black', linewidth=1)

ax.set_title(
    r'График 1. Зависимость $\Delta N \sin^4(\theta/2)$ от угла рассеяния $\theta$',
    fontsize=16,
)

ax.set_xlabel(r'Угол рассеяния $\theta$, град', fontsize=13)

ax.set_ylabel(r'$\Delta N \sin^4(\theta/2)$', fontsize=13)

ax.set_xlim(20, 65)
ax.set_ylim(bottom=0)

ax.grid(True, alpha=0.3)
ax.legend(fontsize=11)

plt.tight_layout()
plt.show()
