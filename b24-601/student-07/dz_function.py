
from time import perf_counter


def make_report(title, *values, unit="В", **metadata):
    """Создаёт строковый отчёт по измерениям."""
    if values:
        average = sum(values) / len(values)
        average_text = f"{average:g} {unit}"
    else:
        average_text = "нет данных"

    lines = [
        f"Заголовок: {title}",
        f"Количество значений: {len(values)}",
        f"Среднее значение: {average_text}",
        f"Единица измерения: {unit}",
    ]

    for key, value in metadata.items():
        lines.append(f"{key}: {value}")

    return "\n".join(lines)


def measure_execution_time(func, *args, **kwargs):
    """Возвращает результат функции и время её выполнения."""
    start = perf_counter()
    result = func(*args, **kwargs)
    elapsed = perf_counter() - start
    return result, elapsed


# 1. Вызов с явно записанными именованными аргументами
report1 = make_report(
    "Измерение напряжения",
    12, 15, 18,
    unit="В",
    source="датчик",
    room="лаборатория"
)
print(report1)

print()

# 2. Вызов с распаковкой списка и словаря
measurements = [10, 20, 30, 40]
metadata = {
    "source": "мультиметр",
    "room": "кабинет 101"
}

report2 = make_report(
    "Повторные измерения",
    *measurements,
    unit="В",
    **metadata
)
print(report2)

print()

# 3. Измерение времени выполнения функции
report, elapsed = measure_execution_time(
    make_report,
    "Тест производительности",
    *measurements,
    unit="В",
    **metadata
)

print("Отчёт:")
print(report)
print(f"Время выполнения: {elapsed:.8f} секунд")
