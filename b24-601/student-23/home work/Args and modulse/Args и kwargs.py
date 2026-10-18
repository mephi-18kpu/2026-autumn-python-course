import time
from collections.abc import Callable

def measure_execution_time(
        function: Callable[..., object],
        *args: object,
        **kwargs: object,
) -> tuple[object, float]:
    start_time = time.time()
    result = function(*args, **kwargs)
    stop_time = time.time()
    return result, stop_time - start_time

def make_report(
        title: str,
        *values: float,
        unit: str = "B",
        **metadata: str,
) -> str:

    count = len(values)

    if count == 0:
        average_str = "нет данных"
    else:
        average = sum(values) / count
        average_str = f"{average:.2f}"

    metadata_lines = []
    for key, value in metadata.items():
        metadata_lines.append(f" {key}: {value}")

    metadata_str = "\n".join(metadata_lines) if metadata_lines else " (нет данных)"

    report = (
        f"=== {title} ===\n"
        f"Количество измерений: {count}\n"
        f"Среднее значение: {average_str} {unit}\n"
        f"Дополнительные сведения:\n"
        f"{metadata_str}"

    )
    return report


if __name__ == "__main__":
    print("=" * 60)
    print("ВЫЗОВ 1: Явные именованные аргументы")
    print("=" * 60)

    report1 = make_report(
        "Измерения напряжения",
        5.2, 5.3, 5.1, 5.4, 5.2,
        unit="мВ",
        source="датчик А",
        room="лаборатория 3",
        operator="Иванов"
    )
    print(report1)

    print("\n" + "=" * 60)
    print("ВЫЗОВ 2: Распаковка через * и **")
    print("=" * 60)

    measurements = [10.5, 10.7, 10.3, 10.8]
    extra_info = {
        "source": "датчик Б",
        "room": "лаборатория 5",
        "date": "2026-10-18"
    }

    report2 = make_report(
        "Измерения тока",
        *measurements,
        unit="мА",
        **extra_info
    )
    print(report2)

    print("\n" + "=" * 60)
    print("ВЫЗОВ 3: Пустой список значений")
    print("=" * 60)

    report3 = make_report(
        "Пустой отчёт",
        unit="В",
        source="нет данных"
    )
    print(report3)

    print("\n" + "=" * 60)
    print("ЗАМЕР ВРЕМЕНИ через measure_execution_time")
    print("=" * 60)

    result, elapsed = measure_execution_time(
        make_report,
        "Тестовые измерения",
        1.0, 2.0, 3.0, 4.0, 5.0,
        unit="В",
        source="тестовый датчик"
    )

    print(result)
    print(f"\nВремя выполнения: {elapsed:.6f} с")