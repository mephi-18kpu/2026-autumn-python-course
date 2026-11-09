"""Выбор измерений, превышающих заданный порог."""

def select_high_measurements(
    measurements: list[float],
    threshold: float,
) -> list[float]:
    """Возвращает новый список значений выше порога."""
    high_measurements = []

    for measurement in measurements:
        if measurement > threshold:
            high_measurements.append(measurement)

    return high_measurements


raw_measurements = input("Введите измерения через пробел: ")
measurements = [float(value) for value in raw_measurements.split()]
threshold = float(input("Введите порог: "))

high_measurements = select_high_measurements(measurements, threshold)
print(f"Измерения выше порога: {high_measurements}")
