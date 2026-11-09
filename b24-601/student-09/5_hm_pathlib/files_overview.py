"""Обзор текстовых файлов в каталогах data/series и data/angles."""

# System imports
from pathlib import Path

# External imports

# User imports

#############################################


script_directory = Path(__file__).resolve().parent
data_directories = [
    script_directory / "data" / "series",
    script_directory / "data" / "angles",
]
results_directory = script_directory / "results"
results_directory.mkdir(exist_ok=True)

report_lines = ["ОБЗОР ФАЙЛОВ ДАННЫХ", ""]
all_files = []
total_non_empty_lines = 0
largest_file = None
largest_file_line_count = -1
largest_file_text = ""

for data_directory in data_directories:
    report_lines.append(f"Каталог: {data_directory.name}")
    text_files = sorted(
        path for path in data_directory.iterdir()
        if path.is_file() and path.suffix == ".txt"
    )

    if not text_files:
        report_lines.append("Файлы .txt не найдены.")
        report_lines.append("")
        continue

    directory_largest_name = None
    directory_largest_count = -1
    directory_total = 0

    for file_path in text_files:
        content = file_path.read_text(encoding="utf-8")
        non_empty_lines = [
            line for line in content.splitlines()
            if line.strip()
        ]
        line_count = len(non_empty_lines)
        first_line = non_empty_lines[0] if non_empty_lines else "нет"
        last_line = non_empty_lines[-1] if non_empty_lines else "нет"

        directory_total += line_count
        total_non_empty_lines += line_count
        all_files.append((file_path, line_count, content))

        report_lines.extend([
            f"Файл: {file_path.name}",
            f"Количество непустых строк: {line_count}",
            f"Первая непустая строка: {first_line}",
            f"Последняя непустая строка: {last_line}",
            "",
        ])

        if line_count > directory_largest_count:
            directory_largest_count = line_count
            directory_largest_name = file_path.name

        if line_count > largest_file_line_count:
            largest_file_line_count = line_count
            largest_file = file_path
            largest_file_text = content

    report_lines.extend([
        f"Всего непустых строк в каталоге: {directory_total}",
        f"Файл с наибольшим количеством строк в каталоге: "
        f"{directory_largest_name} ({directory_largest_count})",
        "",
    ])

report_lines.extend([
    f"Общее количество непустых строк во всех файлах: {total_non_empty_lines}",
    f"Самый большой файл во всём наборе: "
    f"{largest_file.name if largest_file else 'нет'} "
    f"({largest_file_line_count if largest_file else 0} непустых строк)",
])

(results_directory / "files_report.txt").write_text(
    "\n".join(report_lines) + "\n",
    encoding="utf-8",
)

if largest_file is not None:
    (results_directory / "largest_file.txt").write_text(
        largest_file_text,
        encoding="utf-8",
    )
else:
    (results_directory / "largest_file.txt").write_text(
        "",
        encoding="utf-8",
    )

print(f"Всего непустых строк: {total_non_empty_lines}")
print(f"Отчёт сохранён: {results_directory / 'files_report.txt'}")
print(f"Содержимое самого большого файла сохранено: "
      f"{results_directory / 'largest_file.txt'}")
