import matplotlib.pyplot as plt
import numpy as np

# --- ДАННЫЕ ---
# Угол 9 градусов
U_9 = [20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0, 25.5, 26.0, 26.5, 27.0]
R_9 = [1, 8, 29, 54, 77, 98, 121.5, 145, 165, 186, 203, 218, 237, 258]
U0_9 = 20.5

# Угол 10 градусов
U_10 = [18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0]
R_10 = [1, 11, 36, 63, 89, 110, 130, 150]
U0_10 = 18.5

# Угол 11 градусов
U_11 = [16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0]
R_11 = [0, 2, 21, 57, 75, 99, 119, 142, 159, 176, 192, 214]
U0_11 = 16.5

# --- РАСЧЕТ ПОГРЕШНОСТЕЙ ---
# Погрешность напряжения (половина шага 0.5 кВ)
err_U_9 = [0.25] * len(U_9)
err_U_10 = [0.25] * len(U_10)
err_U_11 = [0.25] * len(U_11)

# Погрешность интенсивности (корень из R по статистике Пуассона)
err_R_9 = np.sqrt(R_9)
err_R_10 = np.sqrt(R_10)
err_R_11 = np.sqrt(R_11)

# --- ПОСТРОЕНИЕ ГРАФИКА ---
plt.figure(figsize=(10, 6))

# Строим точки с крестиками погрешностей (errorbar)
# fmt='-o' означает линию с точками, capsize=3 - размер "усиков" погрешности
plt.errorbar(U_9, R_9, xerr=err_U_9, yerr=err_R_9, fmt='-o', color='blue',
             capsize=3, elinewidth=1, alpha=0.8, label=r'\(\theta = 9^\circ\)')
plt.errorbar(U_10, R_10, xerr=err_U_10, yerr=err_R_10, fmt='-s', color='red',
             capsize=3, elinewidth=1, alpha=0.8, label=r'\(\theta = 10^\circ\)')
plt.errorbar(U_11, R_11, xerr=err_U_11, yerr=err_R_11, fmt='-^', color='green',
             capsize=3, elinewidth=1, alpha=0.8, label=r'\(\theta = 11^\circ\)')

# Вертикальные линии U0
plt.axvline(x=U0_9, color='blue', linestyle='--', alpha=0.5)
plt.axvline(x=U0_10, color='red', linestyle='--', alpha=0.5)
plt.axvline(x=U0_11, color='green', linestyle='--', alpha=0.5)

# Подписи U0
plt.text(U0_9 - 0.2, 250, f'U0 = {U0_9} кВ', color='blue', rotation=90, verticalalignment='top')
plt.text(U0_10 - 0.2, 250, f'U0 = {U0_10} кВ', color='red', rotation=90, verticalalignment='top')
plt.text(U0_11 - 0.2, 250, f'U0 = {U0_11} кВ', color='green', rotation=90, verticalalignment='top')

# Оформление
plt.title('Изохроматы тормозного рентгеновского излучения (с погрешностями)', fontsize=14, fontweight='bold')
plt.xlabel('Напряжение на трубке U, кВ', fontsize=12)
plt.ylabel('Интенсивность излучения R, имп/с', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(fontsize=12)

plt.xlim(15, 28)
plt.ylim(0, 270)

plt.show()
