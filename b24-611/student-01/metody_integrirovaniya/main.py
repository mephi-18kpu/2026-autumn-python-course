import numpy as np
import matplotlib.pyplot as plt

# мы помним, что при импортироовании
    # integration_methods у нас открывается файл init, атрибутами integration_methods
    # становятся все функции и переменные которые описаны в __init__.
    # Ну мы их и импортируем прямо сюда
from integration_methods import (
    Integrand,
    integrate_left_rectangles,
    integrate_right_rectangles,
    integrate_midpoint_rectangles,
    integrate_trapezoid,
    integrate_simpson,
)

if __name__ == "__main__":
    podintegralnaya_funktsiya: Integrand = lambda x: np.exp(x) # мы сказали,
    # что подыинтегральная функция - это e^x.
    # Причём обратим внимание, что мы написали тип этой подынтегральной функции - Integrand
    tochnoe_znachenie = np.e - 1.0 # если по честному посчитать интеграл
    print(f"Точное значение интеграла: {tochnoe_znachenie:.8f}")

    kolichestvo_uzlov = [3, 5, 9, 17, 33, 65] # количество узлов вычисляется по формуле
    # (предыдущее - 1) * 2 + 1. Именно за счёт этого каждый раз у нас шаг будет уменьшаться в два раза.
    #65-ти точек достаточно для данной задачи

    metody = [
        ("Левые прямоугольники", integrate_left_rectangles),
        ("Правые прямоугольники", integrate_right_rectangles),
        ("Средние прямоугольники", integrate_midpoint_rectangles),
        ("Трапеции", integrate_trapezoid),
        ("Симпсон", integrate_simpson)
    ]

    rezultaty = {}
    for element in metody:
        nazvanie = element[0]
        rezultaty[nazvanie] = [] # это будет словарь, где ключ - это название метода
        # (например, правые прямоугольники), а значение по ключу - это
        # список из погрешностей каждая из которых отвечает определённому количеству узлов.
        # таким образом, мы будем проверять: как изменяется погрешность вычисления интеграла
        # при уменьшении интервала вдвое
    shagi = []

    print(f"{'Метод':<25} | {'Узлы':<5} | {'Шаг':<10} | {'Результат':<12} | {'Погрешность'}")
    print("-" * 75) # сводная таблица.
    # Такой метод, такое количество точек, такой шаг, такая погрешность

    for uzly_count in kolichestvo_uzlov: # начинаем перебирать разные варианты количества узлов
        uzly = np.linspace(0.0, 1.0, uzly_count, dtype=np.float64)
        shag = uzly[1] - uzly[0]
        shagi.append(shag) # список, какие у нас бывают шаги. тут чисто для удобства - быстро вспомнить

        for nazvanie, metod in metody:
            rezultat = metod(uzly, podintegralnaya_funktsiya) # когда мы пишем metod, мы
            # автоматически вызываем функцию, которую объявили в списке metody.
            # И мы передаём ей аргументы - uzly и подынтегральную функцию
            pogreshnost = abs(rezultat - tochnoe_znachenie)
            rezultaty[nazvanie].append(pogreshnost) # добавляем погрешность по данному методу.
            # Сначала добавится погрешность для 3-х узлов, потом для 5-ти, потом для 9-ти - и так далее

            print(f"{nazvanie:<25} | {uzly_count:<5} | {shag:<10.4f} | {rezultat:<12.6f} | {pogreshnost:.2e}")
            # выод сводной таблицы. .4f означает 4 знака после запятой, .2e - экспоненциальный формат
            # 2 знака после запятой

    # наконец, приступаем к построению графиков
    fig, ax = plt.subplots(figsize=(10, 6)) # создаём окно

    for nazvanie, _ in metody:
        ax.loglog(shagi, rezultaty[nazvanie], marker="o", label=nazvanie) # по оси x у нас будет
        # используемый шаг, по оси y - погрешность, полученная при таком количесстве шагов.
        # А разные методы мы реализуем тем, что построим разные кривые для каждого метода

    ax.set_xlabel("Шаг сетки (h)")
    ax.set_ylabel("Абсолютная погрешность")
    ax.set_title("Сравнение погрешностей методов численного интегрирования")
    ax.grid(True, which="both", ls="--")
    ax.legend()


    plt.show()

