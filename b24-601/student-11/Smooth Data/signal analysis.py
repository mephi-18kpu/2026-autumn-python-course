# System imports
from pathlib import Path

# External imports
import matplotlib

matplotlib.use("Agg")  # сохраняем в файл, окно не нужно
import matplotlib.pyplot as plt
import numpy as np

# User imports

#############################################


BASE_DIRECTORY = Path(__file__).resolve().parent
DATA_DIRECTORY = BASE_DIRECTORY / "data"
RESULTS_DIRECTORY = BASE_DIRECTORY / "results"

WINDOW_SIZES = (5, 21, 51)
PLOT_START_SECONDS = 0.0
PLOT_END_SECONDS = 2.0


def moving_average(values, window_size: int) -> np.ndarray:
    result_length = values.size - window_size + 1
    result = np.empty(result_length, dtype=float)
    for start in range(result_length):
        result[start] = np.mean(values[start : start + window_size])
    return result


def window_center_times(time_values: np.ndarray, window_size: int) -> np.ndarray:
    half_window = window_size // 2
    result_length = time_values.size - window_size + 1
    return time_values[half_window : half_window + result_length]


def load_table(path: Path) -> np.ndarray:
    table = np.loadtxt(path, delimiter="\t", comments="#", encoding="utf-8")
    return table


def main() -> None:
    # Загрузка
    sensor_table = load_table(DATA_DIRECTORY / "sensor_data.txt")
    clean_table = load_table(DATA_DIRECTORY / "clean_signal.txt")

    print(f"Количество измерений: {sensor_table.shape[0]}")
    print(f"Форма таблицы: {sensor_table.shape}")
    print(f"Начальное время: {sensor_table[0, 0]:.6f} с")
    print(f"Конечное время: {sensor_table[-1, 0]:.6f} с")

    time_values = sensor_table[:, 0]
    sensor_values = sensor_table[:, 1]
    clean_values = clean_table[:, 1]

    time_step = float(np.mean(np.diff(time_values)))
    samples_per_second = 1.0 / time_step

    print(f"\nШаг времени: {time_step:.6f} с")
    print(f"Измерений в секунду: {samples_per_second:.1f}")

    # Скользящее среднее для окон 5, 21, 51
    smoothed = {}
    for window_size in WINDOW_SIZES:
        values = moving_average(sensor_values, window_size)
        times = window_center_times(time_values, window_size)
        smoothed[window_size] = (times, values)

    print("\n=== Сглаженные сигналы ===")
    for window_size, (times, values) in smoothed.items():
        print(
            f"Окно {window_size:>2}: точек {values.size}, "
            f"время {times[0]:.3f}...{times[-1]:.3f} с"
        )

    # График
    RESULTS_DIRECTORY.mkdir(exist_ok=True)

    figure, axes = plt.subplots(figsize=(12, 6))
    raw_mask = (time_values >= PLOT_START_SECONDS) & (time_values <= PLOT_END_SECONDS)
    axes.plot(
        time_values[raw_mask],
        sensor_values[raw_mask],
        color="gray",
        alpha=0.4,
        label="Исходный сигнал",
    )
    for window_size, (times, values) in smoothed.items():
        mask = (times >= PLOT_START_SECONDS) & (times <= PLOT_END_SECONDS)
        axes.plot(times[mask], values[mask], linewidth=1.8, label=f"Окно {window_size}")

    axes.set_xlabel("Время, с")
    axes.set_ylabel("Показание датчика, усл. ед.")
    axes.set_title("Скользящее среднее с разными размерами окна (0-2 с)")
    axes.grid(True)
    axes.legend()
    figure.tight_layout()

    # Сохранение графика и таблиц
    figure.savefig(RESULTS_DIRECTORY / "smoothing.png", dpi=150)
    plt.close(figure)

    for window_size, (times, values) in smoothed.items():
        np.savetxt(
            RESULTS_DIRECTORY / f"smoothed_{window_size}.txt",
            np.column_stack((times, values)),
            fmt="%.6f",
            delimiter="\t",
            header=(
                f"Скользящее среднее, окно {window_size}.\n"
                "Время (с)\tСглаженное значение (усл. ед.)"
            ),
            encoding="utf-8",
        )

    # Сравнение с чистым сигналом на тех же временных позициях
    print("\n=== Сравнение с clean_signal.txt ===")
    print(
        f"{'Окно':>6} {'RMSE':>8} {'Остаточный шум':>15} "
        f"{'Искажение формы':>16} {'Макс. пик':>10} {'Пик чист.':>10}"
    )

    # Для исходного сигнала (окно 1 = без сглаживания)
    raw_rmse = float(np.sqrt(np.mean((sensor_values - clean_values) ** 2)))
    raw_mask_stats = (time_values >= PLOT_START_SECONDS) & (time_values <= PLOT_END_SECONDS)
    print(
        f"{'без':>6} {raw_rmse:8.3f} {raw_rmse:15.3f} {'-':>16} "
        f"{sensor_values[raw_mask_stats].max():10.3f} {clean_values[raw_mask_stats].max():10.3f}"
    )

    for window_size, (times, values) in smoothed.items():
        half_window = window_size // 2
        clean_same = clean_values[half_window : half_window + values.size]

        # Полная ошибка сглаженного сигнала относительно чистого
        rmse = float(np.sqrt(np.mean((values - clean_same) ** 2)))

        # Остаточный шум: чистый сигнал, пропущенный через то же окно, - это
        # "идеальный" результат сглаживания; всё сверх него - оставшийся шум.
        clean_smoothed = moving_average(clean_values, window_size)
        residual_noise = float(np.sqrt(np.mean((values - clean_smoothed) ** 2)))

        # Искажение формы: насколько само окно изменило чистый сигнал (потеря быстрых колебаний)
        distortion = float(np.sqrt(np.mean((clean_smoothed - clean_same) ** 2)))

        mask = (times >= PLOT_START_SECONDS) & (times <= PLOT_END_SECONDS)
        print(
            f"{window_size:>6} {rmse:8.3f} {residual_noise:15.3f} {distortion:16.3f} "
            f"{values[mask].max():10.3f} {clean_same[mask].max():10.3f}"
        )

    print("\nГрафик и таблицы сохранены в", RESULTS_DIRECTORY)


if __name__ == "__main__":
    main()
