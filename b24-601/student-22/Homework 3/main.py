from pathlib import Path

base_path = Path(r"C:\Python\2026-autumn-python-course\code-examples\NumPy и Matplotlib")
data_dir = base_path / "data"
series_dir = data_dir / "series"
angles_dir = data_dir / "angles"
results_dir = base_path / "results"

results_dir.mkdir(exist_ok=True)

report_text = ""
total_non_empty_lines = 0
global_max_lines = -1
global_max_file_path = None

folders_to_process = [("series", series_dir), ("angles", angles_dir)]

for folder_name, folder_path in folders_to_process:

    if not folder_path.exists():
        continue

    folder_max_lines = -1
    folder_best_file_name = ""

    files_list = []

    for file_path in folder_path.iterdir():
        if file_path.is_file() and file_path.suffix == ".txt" and file_path.name != "README.md":
            files_list.append(file_path)

    files_list.sort()

    for file_path in files_list:
        # Читаем текст в UTF-8
        file = open(file_path, "r", encoding="utf-8")
        lines = file.readlines()
        file.close()

        non_empty_count = 0
        first_line = ""
        last_line = ""

        for line in lines:
            clean_line = line.strip()

            if clean_line != "":
                non_empty_count = non_empty_count + 1

                if first_line == "":
                    first_line = clean_line

                last_line = clean_line

        total_non_empty_lines = total_non_empty_lines + non_empty_count

        if non_empty_count > folder_max_lines:
            folder_max_lines = non_empty_count
            folder_best_file_name = file_path.name

        if non_empty_count > global_max_lines:
            global_max_lines = non_empty_count
            global_max_file_path = file_path

        report_text = report_text + "Файл: " + file_path.name + " (папка: " + folder_name + ")\n"
        report_text = report_text + "  Количество непустых строк: " + str(non_empty_count) + "\n"
        report_text = report_text + "  Первая непустая строка: " + first_line + "\n"
        report_text = report_text + "  Последняя непустая строка: " + last_line + "\n"

    report_text = report_text + "\nРезультаты в " + folder_name.upper() + ":\n"
    report_text = report_text + "Максимум строк в файле: " + folder_best_file_name + " (" + str(folder_max_lines) + " строк)\n"

if global_max_file_path is not None:
    original_file = open(global_max_file_path, "r", encoding="utf-8")
    original_content = original_file.read()
    original_file.close()

    largest_copy = open(results_dir / "largest_file.txt", "w", encoding="utf-8")
    largest_copy.write(original_content)
    largest_copy.close()

    report_text = report_text + "Результаты:\n"
    report_text = report_text + "Общее количество непустых строк во всех обработанных файлах " + str(total_non_empty_lines) + "\n"
    report_text = report_text + "Файл с наибольшим количеством строк во всем наборе " + global_max_file_path.name + "\n"
    report_text = report_text + "Его исходный путь: " + str(global_max_file_path) + "\n"

report_file = open(results_dir / "files_report.txt", "w", encoding="utf-8")
report_file.write(report_text)
report_file.close()

print("Результс", results_dir)