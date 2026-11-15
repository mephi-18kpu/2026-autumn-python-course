"""Отчёт по измерениям: *args, **kwargs и замер времени."""

# System imports
import time
from collections.abc import Callable

# External imports

# User imports

#############################################


def make_report(
    title: str,
    *values: float,
    unit: str = "В",
    **metadata: str,
) -> str:
    """Формирует текстовый отчёт по измерениям.

    Args:
        title: Заголовок отчёта.
        *values: Любое количество числовых измерений.
        unit: Единица измерения.
        **metadata: Дополнительные текстовые сведения.

    Returns:
        Строка отчёта.
    """
    lines = [title, "=" * len(title), ""]
    lines.append(f"Количество значений: {len(values)}")
    lines.append(f"Единица измерения: {unit}")

    if values:
        average = sum(values) / len(values)
        lines.append(f"Среднее значение: {average:.3f} {unit}")
    else:
        lines.append("Среднее значение: нет данных")

    if metadata:
        lines.append("Дополнительные сведения:")
        for key, value in metadata.items():
            lines.append(f"  {key}: {value}")
    else:
        lines.append("Дополнительные сведения: нет")

    return "\n".join(lines)


def measure_execution_time(
    function: Callable[..., object],
    *args: object,
    **kwargs: object,
) -> tuple[object, float]:
    """Вызывает функцию и возвращает результат вместе со временем.

    Args:
        function: Вызываемая функция.
        *args: Её позиционные аргументы.
        **kwargs: Её именованные аргументы.

    Returns:
        Результат функции и время выполнения в секундах.
    """
    start_time = time.time()
    result = function(*args, **kwargs)
    stop_time = time.time()

    return result, stop_time - start_time


# ---- Вызов 1: явные именованные аргументы ----

report_1, elapsed_1 = measure_execution_time(
    make_report,
    "Измерения, вызов 1",
    5.2,
    5.4,
    5.1,
    unit="В",
    source="датчик",
    room="лаборатория",
)

print(report_1)
print(f"Время выполнения: {elapsed_1:.9f} с")
print()

# ---- Вызов 2: распаковка списка и словаря ----

title = "Измерения, вызов 2"
values = [1.5, 1.6, 1.7, 1.55]
options = {"unit": "мВ", "source": "измеритель", "room": "цех"}

report_2, elapsed_2 = measure_execution_time(
    make_report,
    title,
    *values,
    **options,
)

print(report_2)
print(f"Время выполнения: {elapsed_2:.9f} с")
print()

# ---- Вызов 3 (дополнительно): без значений ----

report_3, elapsed_3 = measure_execution_time(
    make_report,
    "Пустой отчёт",
    unit="А",
    source="датчик не подключён",
)

print(report_3)
print(f"Время выполнения: {elapsed_3:.9f} с")
