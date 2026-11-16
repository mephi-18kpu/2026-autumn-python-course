import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def main():
    # 1. Настройка путей
    input_dir = Path("data/series")
    output_dir = Path("results")

    output_dir.mkdir(parents=True, exist_ok=True)

    # 2. Поиск и сортировка файлов
    files = sorted([f for f in input_dir.iterdir() if f.is_file() and f.suffix == '.txt'])

    if not files:
        print("Файлы .txt не найдены в папке data/series")
        return

    stats = []
    data_dict = {}

    # 3. Обработка каждого файла
    for file_path in files:
        data = np.loadtxt(file_path)
        data_dict[file_path.name] = data

        count = len(data)
        min_val = np.min(data)
        max_val = np.max(data)
        mean_val = np.mean(data)
        std_val = np.std(data)

        above_mean = np.sum(data > mean_val)

        stats.append({
            'name': file_path.name,
            'count': count,
            'min': min_val,
            'max': max_val,
            'mean': mean_val,
            'std': std_val,
            'above_mean': above_mean
        })

    # 4. Определение экстремумов
    max_mean_file = max(stats, key=lambda x: x['mean'])
    min_std_file = min(stats, key=lambda x: x['std'])

    # 5. Запись текстового отчета
    report_path = output_dir / "series_report.txt"
    with open(report_path, 'w', encoding='utf-8') as f:
        for s in stats:
            f.write(f"Файл: {s['name']}\n")
            f.write(f"  Количество значений: {s['count']}\n")
            f.write(f"  Минимум: {s['min']:.2f}\n")
            f.write(f"  Максимум: {s['max']:.2f}\n")
            f.write(f"  Среднее: {s['mean']:.2f}\n")
            f.write(f"  Стандартное отклонение: {s['std']:.2f}\n")
            f.write(f"  Значений выше среднего: {s['above_mean']}\n\n")

        f.write("--- ИТОГИ ---\n")
        f.write(f"Наибольшее среднее у файла: {max_mean_file['name']} ({max_mean_file['mean']:.2f})\n")
        f.write(f"Наименьшее стандартное отклонение у файла: {min_std_file['name']} ({min_std_file['std']:.2f})\n")

    # 6. Построение графика
    fig, ax = plt.subplots(figsize=(10, 6))

    # Для каждого файла создаем свой массив индексов (т.к. длины разные)
    for filename, data in data_dict.items():
        indices = np.arange(len(data))
        ax.plot(indices, data, marker='o', label=filename)

    ax.set_xlabel("Индекс элемента")
    ax.set_ylabel("Значение")
    ax.set_title("Сравнение серий измерений")
    ax.grid(True)
    ax.legend()

    plt.savefig(output_dir / "series.png", dpi=300, bbox_inches='tight')
    plt.close()

    print("Обработка завершена. Результаты сохранены в папке 'results'.")


if __name__ == "__main__":
    main()