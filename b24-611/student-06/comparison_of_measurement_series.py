from pathlib import Path
import numpy as np

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data" / "series"
RESULTS_DIR = BASE_DIR / "results"

threshold = float(input("Введите числовой порог для серий: "))

reports = []
best_mean_value = -float("inf")
best_mean_file = ""
best_std_value = float("inf")
best_std_file = ""

if not DATA_DIR.exists():
    print(f"Ошибка: Директория {DATA_DIR} не найдена.")
    exit(1)

for file_path in sorted(DATA_DIR.iterdir()):
    if file_path.is_file() and file_path.suffix == ".txt":
        try:
            data = np.loadtxt(file_path)
            if data.ndim == 0:
                data = np.array([data])
        except Exception as e:
            print(f"Не удалось прочитать файл {file_path.name}: {e}")
            continue

        if data.size == 0:
            continue

        count = len(data)
        min_value = np.min(data)
        max_value = np.max(data)
        mean_value = np.mean(data)
        std_value = np.std(data)
        above_threshold = int(np.sum(data > threshold))

        file_report = (
            f"Файл: {file_path.name}\n"
            f"  Количество измерений: {count}\n"
            f"  Минимум: {min_value:.4f}\n"
            f"  Максимум: {max_value:.4f}\n"
            f"  Среднее значение: {mean_value:.4f}\n"
            f"  Стандартное отклонение: {std_value:.4f}\n"
            f"  Значений выше порога ({threshold}): {above_threshold}\n"
        )
        reports.append(file_report)

        # 4) Сравнение серий между собой
        if mean_value > best_mean_value:
            best_mean_value = mean_value
            best_mean_file = file_path.name

        if std_value < best_std_value:
            best_std_value = std_value
            best_std_file = file_path.name

# 5) Создание каталога results и запись отчета
RESULTS_DIR.mkdir(parents=True, exist_ok=True)
report_file_path = RESULTS_DIR / "series_report.txt"

with open(report_file_path, "w", encoding="utf-8") as f:
    f.write("=== ОТЧЕТ ПО СЕРИЯМ ИЗМЕРЕНИЙ ===\n")
    f.write(f"Заданный порог: {threshold}\n\n")

    f.write("--- Результаты по каждому файлу ---\n")
    for rep in reports:
        f.write(rep + "\n")

    f.write("--- Результаты сравнения ---\n")
    if reports:
        f.write(f"Файл с наибольшим средним значением: {best_mean_file} (Среднее: {best_mean_value:.4f})\n")
        f.write(f"Файл с наименьшим стандартным отклонением: {best_std_file} (Отклонение: {std_value:.4f})\n")
    else:
        f.write("Нет данных для сравнения (файлы .txt отсутствуют или пусты).\n")

print(f"Анализ завершен. Отчет успешно сохранен/обновлен в {report_file_path.relative_to(BASE_DIR)}")
