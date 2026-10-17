"""Программа для анализа введённых оценок."""

# System imports

# External imports

# User imports
from other_file import calculate_average, get_good_scores

#############################################


print("Значение __name__ в main.py:", __name__)  # При прямом запуске: __main__.
print("Значение __file__ в main.py:", __file__)  # Путь к main.py.

entered_scores = input("Введите оценки через пробел: ")
scores = [int(value) for value in entered_scores.split()]

if scores:
    good_scores = get_good_scores(scores)

    print("Средняя оценка:", calculate_average(scores))  # Для ввода 5 3 4 5: 4.25.
    print("Оценок не ниже четырёх:", len(good_scores))  # Для ввода 5 3 4 5: 3.
    print("Сами оценки:", good_scores)  # Для ввода 5 3 4 5: [5, 4, 5].
else:
    print("Оценки не введены")  # Если нажать Enter без чисел.
