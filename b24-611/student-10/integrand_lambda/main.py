import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import matplotlib.pyplot as plt
from integration_methods import (
    Integrand,
    integrate_midpoint_rectangles,
    integrate_left_rectangles,
    integrate_right_rectangles,
    integrate_trapezoid,
    integrate_simpson,
)

def run():
    integrand: Integrand = lambda x: np.exp(x)
    true_value = float(np.exp(1.0) - 1.0)
    n_intervals = [10, 20, 40, 80, 160, 320]
    
    steps = []
    errors_left = []
    errors_right = []
    errors_mid = []
    errors_trap = []
    errors_simp = []
    
    print('-'*115)
    print(f'{"N":>6} | {"шаг h":>10} | {"погр левые":>14} | {"погр правые":>14} | {"погр средние":>14} | {"погр трапец.":>14} | {"погр Симпсон":>14}')
    print('-'*115)
    
    for n in n_intervals:
        nodes = np.linspace(0.0, 1.0, n + 1, dtype=np.float64)
        h = float(nodes[1] - nodes[0])
        steps.append(h)
        
        err_left = abs(integrate_left_rectangles(nodes, integrand) - true_value)
        err_right = abs(integrate_right_rectangles(nodes, integrand) - true_value)
        err_mid = abs(integrate_midpoint_rectangles(nodes, integrand) - true_value)
        err_trap = abs(integrate_trapezoid(nodes, integrand) - true_value)
        err_simp = abs(integrate_simpson(nodes, integrand) - true_value)
        
        errors_left.append(err_left)
        errors_right.append(err_right)
        errors_mid.append(err_mid)
        errors_trap.append(err_trap)
        errors_simp.append(err_simp)
        
        print(f'{n:6d} | {h:10.5f} | {err_left:14.2e} | {err_right:14.2e} | {err_mid:14.2e} | {err_trap:14.2e} | {err_simp:14.2e}')
        
    print('-'*115)
    
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.loglog(steps, errors_left, '-o', label='левые прямоугольники (O(h))')
    ax.loglog(steps, errors_right, '-s', label='правые прямоугольники (O(h))')
    ax.loglog(steps, errors_mid, '-^', label='средние прямоугольники (O(h^2))')
    ax.loglog(steps, errors_trap, '-d', label='метод трапеций (O(h^2))')
    ax.loglog(steps, errors_simp, '-X', label='метод Симпсона (O(h^4))')
    
    ax.set_title('зависимость абсолютной погрешности от шага сетки (Log-Log)')
    ax.set_xlabel('шаг сетки (h)')
    ax.set_ylabel('абсолютная погрешность')
    ax.grid(True, which='both', linestyle='--', alpha=0.5)
    ax.legend()
    
    plt.show()

if __name__ == '__main__':
    try:
        run()
    except Exception as e:
        import traceback
        print("ошибка при запуске")
        traceback.print_exc()
        input('\n Нажмите ентер для выхода')


