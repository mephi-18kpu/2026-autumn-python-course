import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def main():
    # 1. Настройка путей
    input_dir = Path("data/angles")
    output_dir = Path("results")
    output_angles_dir = output_dir / "angles"

    output_angles_dir.mkdir(parents=True, exist_ok=True)

    files = sorted([f for f in input_dir.iterdir() if f.is_file() and f.suffix == '.txt'])

    if not files:
        print("Файлы .txt не найдены в папке data/angles")
        return

    report_data = []

    # 2. Обработка каждого файла
    for file_path in files:
        angles_deg = np.loadtxt(file_path)

        angles_rad = np.deg2rad(angles_deg)
        sin_vals = np.sin(angles_rad)
        cos_vals = np.cos(angles_rad)

        stem = file_path.stem

        # Пункт 2: Сохранение текстовых файлов с результатами
        np.savetxt(output_angles_dir / f"{stem}_sin.txt", sin_vals)
        np.savetxt(output_angles_dir / f"{stem}_cos.txt", cos_vals)

        # Пункт 3: Сбор статистики для отчета
        max_angle = np.max(angles_deg)
        count_sin_above_06 = np.sum(sin_vals > 0.6)

        report_data.append({
            'name': file_path.name,
            'max_angle': max_angle,
            'count_above': count_sin_above_06
        })

        #  Пункт 4: Построение графиков
        fig, ax = plt.subplots(figsize=(10, 6))

        dense_deg = np.linspace(0, 180, 500)
        dense_rad = np.deg2rad(dense_deg)

        ax.plot(dense_deg, np.sin(dense_rad), label='sin(x)', color='blue', alpha=0.7)
        ax.plot(dense_deg, np.cos(dense_rad), label='cos(x)', color='orange', alpha=0.7)

        ax.scatter(angles_deg, sin_vals, color='blue', edgecolor='black', zorder=5, s=50, label='Точки sin')
        ax.scatter(angles_deg, cos_vals, color='orange', edgecolor='black', zorder=5, s=50, label='Точки cos')

        ax.set_xlabel("Угол, градусы")
        ax.set_ylabel("Значение функции")
        ax.set_title(f"Тригонометрия для файла: {file_path.name}")
        ax.grid(True)
        ax.legend(loc='best')


        plt.savefig(output_angles_dir / f"{stem}.png", dpi=300, bbox_inches='tight')
        plt.close(fig)

    report_path = output_dir / "angles_report.txt"

    best_file = max(report_data, key=lambda x: x['count_above'])

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("Отчет по тригонометрическому анализу\n")
        f.write("=" * 40 + "\n")
        for data in report_data:
            f.write(f"Файл: {data['name']}\n")
            f.write(f"  Максимальный угол: {data['max_angle']}°\n")
            f.write(f"  Количество sin(x) > 0.6: {data['count_above']}\n\n")

        f.write("-" * 40 + "\n")
        f.write(f"Наибольшее количество sin(x) > 0.6 в файле: {best_file['name']} ({best_file['count_above']} шт.)\n")

    print("Обработка завершена! Все графики и отчеты сохранены в папке 'results'.")


if __name__ == "__main__":
    main()
