"""Функции для обработки оценок и пример их самостоятельного запуска."""

# System imports

# External imports

# User imports

#############################################


def calculate_average(scores: list[int]) -> float:
    """Вычислить среднюю оценку.

    Args:
        scores: Непустой список оценок.

    Returns:
        Средняя оценка.
    """
    return sum(scores) / len(scores)


def get_good_scores(scores: list[int]) -> list[int]:
    """Выбрать оценки не ниже четырёх.

    Args:
        scores: Список оценок.

    Returns:
        Список оценок не ниже четырёх.
    """
    result = []

    for score in scores:
        if score >= 4:
            result.append(score)

    return result


print("Значение __name__ в other_file.py:", __name__)  # __main__ или other_file.
print("Значение __file__ в other_file.py:", __file__)  # Путь к other_file.py.

if __name__ == "__main__":
    example_scores = [5, 3, 4, 5]
    print("Проверка средней оценки:", calculate_average(example_scores))  # 4.25.
    print("Проверка отбора оценок:", get_good_scores(example_scores))  # [5, 4, 5].
