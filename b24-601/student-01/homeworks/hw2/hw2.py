from collections.abc import Callable
import time


def measure_execution_time(
    function: Callable[..., object],
    *args: object,
    **kwargs: object,
) -> tuple[object, float]:
    start_time = time.time()
    result = function(*args, **kwargs)
    return result, time.time() - start_time


def make_report(
    title: str,
    *values: float,
    unit: str = "В",
    **metadata: str,
) -> str:
    count = len(values)
    average = f"{sum(values) / count:.2f} {unit}" if count > 0 else "Нет данных"

    lines = [
        f"Заголовок: {title}",
        f"Количество значений: {count}",
        f"Среднее значение: {average}",
        f"Единица измерения: {unit}",
    ]

    for key, value in metadata.items():
        lines.append(f"{key}: {value}")

    return "\n".join(lines)

print(make_report("Напряжение", 220.1, 219.5, 220.8, unit="В", room="лаборатория"))
print(" ")

measurements = [10.3, 12.4, 12.2, -10.0, 14.89]
params = {"source": "амперметр", "status": "активен", "спартак здесь?": "все спортсмены на месте"}
print(make_report("Ток", *measurements, unit="А", **params))
print(" ")

report_result, elapsed_time = measure_execution_time(
    make_report,
    "Давление",
    source ="клапан",
    unit="кПа",
    device="барометр",
    на_клапан_давит = ")))"
)

print(report_result)
print(f"Время выполнения: {elapsed_time:.9f} сек.")
