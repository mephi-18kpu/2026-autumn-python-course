"""Подсчёт положительных измерений."""

def count_positive_measurements(measurements: list[float]) -> int:
    """Возвращает количество положительных значений."""
    positive_count = 0

    for measurement in measurements:
        if measurement > 0:
            positive_count += 1

    return positive_count


raw_measurements = input("Введите измерения через пробел: ")
measurements = [float(value) for value in raw_measurements.split()]

positive_count = count_positive_measurements(measurements)
print(f"Количество положительных измерений: {positive_count}")
