
from pathlib import Path
from shutil import copyfile

BASE_DIR = Path(__file__).resolve().parent
DATA_DIRS = [BASE_DIR / "data" / "series", BASE_DIR / "data" / "angles"]
RESULTS_DIR = BASE_DIR / "results"

file_infos = []
directory_results = {}

for data_dir in DATA_DIRS:
    if not data_dir.is_dir():
        raise FileNotFoundError(f"Папка не найдена: {data_dir}")

    files = sorted(
        (f for f in data_dir.iterdir() if f.is_file() and f.suffix == ".txt"),
        key=lambda f: f.name
    )

    max_lines_in_dir = -1
    max_file_in_dir = None

    for file in files:
        text = file.read_text(encoding="utf-8")
        lines = text.splitlines()
        non_empty_lines = [line for line in lines if line.strip()]

        count_non_empty = len(non_empty_lines)
        first_line = non_empty_lines[0] if non_empty_lines else "(нет)"
        last_line = non_empty_lines[-1] if non_empty_lines else "(нет)"

        info = {
            "dir": data_dir.name,
            "name": file.name,
            "count": count_non_empty,
            "first": first_line,
            "last": last_line,
            "path": file
        }

        file_infos.append(info)

        if count_non_empty > max_lines_in_dir:
            max_lines_in_dir = count_non_empty
            max_file_in_dir = info

    directory_results[data_dir.name] = max_file_in_dir

if not file_infos:
    raise ValueError("Не найдено ни одного подходящего файла")

global_largest_file = max(file_infos, key=lambda x: x["count"])
total_non_empty_lines = sum(info["count"] for info in file_infos)

RESULTS_DIR.mkdir(parents=True, exist_ok=True)

report_path = RESULTS_DIR / "files_report.txt"

with report_path.open("w", encoding="utf-8") as report:
    report.write("Отчёт по обзору файлов данных\n")
    report.write("=" * 40 + "\n\n")

    for data_dir in DATA_DIRS:
        d_name = data_dir.name
        dir_files = [f for f in file_infos if f["dir"] == d_name]

        report.write(f"Каталог: {d_name}\n")

        if not dir_files:
            report.write("Подходящих файлов нет\n")
            report.write("-" * 40 + "\n")
            continue

        for info in dir_files:
            report.write(f"  Файл: {info['name']}\n")
            report.write(f"    Непустых строк: {info['count']}\n")
            report.write(f"    Первая строка: {info['first']}\n")
            report.write(f"    Последняя строка: {info['last']}\n")

        largest = directory_results[d_name]

        report.write(
            f"Самый большой файл каталога: {largest['name']} "
            f"({largest['count']} непустых строк)\n"
        )
        report.write("-" * 40 + "\n")

    report.write("\nОбщие результаты:\n")
    report.write(f"Всего обработано файлов: {len(file_infos)}\n")
    report.write(
        f"Общее количество непустых строк: "
        f"{total_non_empty_lines}\n"
    )
    report.write(
        f"Файл с наибольшим количеством непустых строк: "
        f"{global_largest_file['name']} "
        f"(каталог: {global_largest_file['dir']}, "
        f"строк: {global_largest_file['count']})\n"
    )

largest_file_out = RESULTS_DIR / "largest_file.txt"
copyfile(global_largest_file["path"], largest_file_out)

print("Анализ завершён!")
print(f"Отчёт сохранён в: {report_path}")
print(f"Самый большой файл скопирован в: {largest_file_out}")
