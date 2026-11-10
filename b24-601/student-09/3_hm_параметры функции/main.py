"""Отчёт по измерениям: позиционные и именованные аргументы."""

# System imports
from collections.abc import Callable
from time import perf_counter

# External imports

# User imports

#############################################


def make_report(title: str, *values: float, unit: str = "В", **metadata: str) -> str:
    """Сформировать отчёт по измерениям.

    Args:
        title: Заголовок отчёта.
        *values: Произвольное количество числовых измерений.
        unit: Единица измерения; передаётся только по имени.
        **metadata: Дополнительные текстовые сведения.

    Returns:
        Готовый текст отчёта.
    """
    lines = [
        title,
        f"Количество измерений: {len(values)}",
    ]

    if values:
        average = sum(values) / len(values)
        lines.append(f"Среднее значение: {average:.3f} {unit}")
    else:
        lines.append("Среднее значение: нет данных")

    lines.append(f"Единица измерения: {unit}")
    lines.append("Дополнительные сведения:")

    if metadata:
        for key, value in metadata.items():
            lines.append(f"{key}: {value}")
    else:
        lines.append("нет")

    return "\n".join(lines)


def measure_execution_time(
    function: Callable[..., object],
    *args: object,
    **kwargs: object,
) -> tuple[object, float]:
    """Вызвать функцию с переданными аргументами и измерить время."""
    start_time = perf_counter()
    result = function(*args, **kwargs)
    elapsed_time = perf_counter() - start_time
    return result, elapsed_time


# Вызов с явно указанными аргументами.
first_report = make_report(
    "Отчёт № 1",
    12.5,
    13.0,
    11.5,
    unit="мВ",
    source="датчик",
    room="лаборатория",
)
print(first_report)

print("\n" + "=" * 40 + "\n")

# Вызов с распаковкой заранее подготовленных списка и словаря.
measurements = [5.1, 5.3, 5.2]
report_options = {
    "unit": "В",
    "source": "вольтметр",
    "room": "аудитория 204",
}
second_report, elapsed = measure_execution_time(
    make_report,
    "Отчёт № 2",
    *measurements,
    **report_options,
)
print(second_report)
print(f"Время формирования отчёта: {elapsed:.8f} с")

print("\n" + "=" * 40 + "\n")

# Отдельная проверка случая без измерений.
print(make_report("Пустой отчёт", unit="А", source="нет данных"))
