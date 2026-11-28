from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

SCRIPT_DIR = Path(__file__).resolve().parent


input_path = SCRIPT_DIR / "data" / "sensor_data.txt"
clean_path = SCRIPT_DIR / "data" / "clean_signal.txt"

results_dir = SCRIPT_DIR / "results"
results_dir.mkdir(parents=True, exist_ok=True)


def load_data(path):
    data = np.loadtxt(path, encoding="utf-8", ndmin=2)

    time_values = data[:, 0]
    sensor_values = data[:, 1]

    return time_values, sensor_values



time_arr, signal_arr = load_data(input_path)


print(f"Количество измерений: {len(signal_arr)}")
print(f"Форма таблицы: {np.shape(signal_arr)}")
print(f"Начальное время: {time_arr[0]}, Конечное время: {time_arr[-1]}")
print(f"Шаг времени (dt): {time_arr[1] - time_arr[0]}")
print(f"Частота измерений: {1 / (time_arr[1] - time_arr[0])} Гц")


def moving_average(data, window_size):
    if not isinstance(window_size, int) or window_size % 2 == 0:
        raise ValueError("Размер окна должен быть нечётным целым числом")
    if window_size < 1 or window_size > len(data):
        raise ValueError("Размер окна должен быть от 1 до длины массива")


    smoothed = []


    for i in range(len(data) - window_size + 1):
        window = data[i: i + window_size]
        smoothed.append(np.mean(window))

    return np.array(smoothed)


windows = [5, 21, 51]
smoothed_results = {}

for w in windows:
    smoothed_results[w] = moving_average(signal_arr, w)
    h = (w - 1) // 2
    time_centered = time_arr[h: len(time_arr) - h]
    smoothed_results[f"time_{w}"] = time_centered

plt.figure(figsize=(12, 6))


plt.plot(time_arr, signal_arr, label="Исходный сигнал (с шумом)", color="gray", alpha=0.5, linewidth=1)


colors = {5: "blue", 21: "green", 51: "red"}

for w in windows:
    t = smoothed_results[f"time_{w}"]
    y = smoothed_results[w]

    mask = (t >= 0) & (t <= 2)

    plt.plot(t[mask], y[mask], label=f"Окно {w}", color=colors[w], linewidth=2)


plt.title("Сглаживание данных датчика скользящим средним")
plt.xlabel("Время (с)")
plt.ylabel("Показание (усл. ед.)")
plt.grid(True)
plt.legend()
plt.xlim(0, 2)


plot_path = results_dir / "smoothing.png"
plt.savefig(plot_path, dpi=150, bbox_inches="tight")
print(f"График сохранен в {plot_path}")
plt.show()


for w in windows:
    t = smoothed_results[f"time_{w}"]
    y = smoothed_results[w]
    output_data = np.column_stack((t, y))

    out_file = results_dir / f"smoothed_{w}.txt"
    np.savetxt(
        out_file,
        output_data,
        fmt="%.6f",
        delimiter="\t",
        header="Время (с)\tСглаженный сигнал",
        encoding="utf-8"
    )
    print(f"Сохранен файл: {out_file}")


clean_time, clean_signal = load_data(clean_path)

print("\n--- Сравнение с чистым сигналом ---")
for w in windows:
    t = smoothed_results[f"time_{w}"]
    y = smoothed_results[w]
    h = (w - 1) // 2
    clean_cropped = clean_signal[h: len(clean_signal) - h]

    error = np.mean(np.abs(y - clean_cropped))
    print(f"Средняя абсолютная ошибка для окна {w}: {error:.4f}")
