
import time


def make_report(title, *values, unit="В", **metadata):
    report = f"--- {title} ---\n"

    count = len(values)
    report += f"Количество значений: {count}\n"

    if count == 0:
        report += "Среднее значение: нет данных\n"
    else:
        mean_val = sum(values) / count
        report += f"Среднее значение: {mean_val:.2f}\n"

    report += f"Единица измерения: {unit}\n"

    if metadata:
        report += "Дополнительно:\n"
        for key, value in metadata.items():
            report += f"  {key}: {value}\n"

    return report


def measure_execution_time(func, *args, **kwargs):
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    elapsed = time.perf_counter() - start_time
    return result, elapsed


if __name__ == "__main__":
    report_1 = make_report(
        "Тест 1",
        10, 20, 30,
        unit="мВ",
        source="датчик",
        room="лаборатория"
    )
    print("Вызов 1:")
    print(report_1)

    title = "Тест 2"
    measurements = [1.5, 2.5, 3.5, 4.5]
    extra_info = {
        "unit": "А",
        "operator": "Иванов"
    }

    report_2 = make_report(title, *measurements, **extra_info)
    print("Вызов 2:")
    print(report_2)

    print("Проверка без измерений:")
    print(make_report("Пустые измерения"))

    result, elapsed = measure_execution_time(
        make_report,
        "Замер",
        5, 6, 7,
        unit="кг",
        author="Python"
    )

    print("Замер времени выполнения:")
    print(result)
    print(f"Прошедшее время: {elapsed:.6f} сек.")
