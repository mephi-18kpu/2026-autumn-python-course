"""Генерация измерений датчика: сумма пяти синусоид с нормальным шумом."""

# System imports
from pathlib import Path

# External imports
import numpy as np

# User imports

#############################################


SAMPLE_RATE_HZ = 500
DURATION_SECONDS = 10.0
FREQUENCIES_HZ = (2.0, 7.0, 12.0, 20.0, 35.0)
AMPLITUDES = (1.0, 0.7, 0.5, 0.35, 0.2)
NOISE_STANDARD_DEVIATION = 0.6
RANDOM_SEED = 42


def main() -> None:
    """Создать и сохранить измерения и отдельный сигнал без шума.

    Файлы записываются в каталог data рядом со скриптом. При повторном
    запуске существующие файлы с теми же именами перезаписываются.
    """
    sample_count = int(SAMPLE_RATE_HZ * DURATION_SECONDS)
    time_values = np.arange(sample_count, dtype=float) / SAMPLE_RATE_HZ
    clean_signal = np.zeros(sample_count, dtype=float)

    for frequency_hz, amplitude in zip(FREQUENCIES_HZ, AMPLITUDES):
        clean_signal += amplitude * np.sin(2 * np.pi * frequency_hz * time_values)

    random_generator = np.random.default_rng(RANDOM_SEED)
    noise = random_generator.normal(
        loc=0.0,
        scale=NOISE_STANDARD_DEVIATION,
        size=sample_count,
    )
    sensor_signal = clean_signal + noise

    output_directory = Path(__file__).resolve().parent / "data"
    output_directory.mkdir(exist_ok=True)
    sensor_path = output_directory / "sensor_data.txt"
    clean_path = output_directory / "clean_signal.txt"

    measurement_header = (
        "Эмуляция показаний датчика: сумма пяти синусоид с нормальным шумом.\n"
        f"Частота измерений: {SAMPLE_RATE_HZ} Гц. "
        f"Длительность записи: {DURATION_SECONDS:g} с.\n"
        f"Частоты синусоид, Гц: {FREQUENCIES_HZ}.\n"
        f"Амплитуды, усл. ед.: {AMPLITUDES}.\n"
        f"Среднее шума: 0. Стандартное отклонение: {NOISE_STANDARD_DEVIATION}. "
        f"Начальное значение генератора: {RANDOM_SEED}.\n"
        "Время (с)\tПоказание датчика (усл. ед.)"
    )
    np.savetxt(
        sensor_path,
        np.column_stack((time_values, sensor_signal)),
        fmt="%.6f",
        delimiter="\t",
        header=measurement_header,
        encoding="utf-8",
    )
    np.savetxt(
        clean_path,
        np.column_stack((time_values, clean_signal)),
        fmt="%.6f",
        delimiter="\t",
        header=(
            "Сигнал без шума для проверки результатов сглаживания.\n"
            "Время (с)\tЗначение сигнала (усл. ед.)"
        ),
        encoding="utf-8",
    )

    print(f"Количество измерений: {sample_count}")
    print(f"Измерения с шумом: {sensor_path}")
    print(f"Сигнал без шума: {clean_path}")


if __name__ == "__main__":
    main()
