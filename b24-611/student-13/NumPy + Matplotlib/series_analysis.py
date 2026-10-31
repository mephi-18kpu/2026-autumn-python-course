# System imports
from pathlib import Path
# External imports
import matplotlib.pyplot as plt
import numpy as np

# User imports

#############################################

script_directory = Path(__file__).resolve().parent.parent
data_directory = script_directory / "data" / "series"

report_directory = data_directory / "results"
report_directory.mkdir(exist_ok=True)
report = report_directory / "series_report.txt"

report_text = ""

fig, ax = plt.subplots(figsize = (12,6))



for path in data_directory.iterdir():
    if path.name == "README.md" or path.name == "results":
        continue
    values = np.loadtxt(path)
    length = len(values)
    report_text += str(path.name)
    report_text += "\nдлина: " + str(length)
    report_text += "\nминимум: " + str(np.min(values))
    report_text += "\nмаксимум: " + str(np.max(values))
    report_text += "\nсреднее: " + str(np.mean(values))
    report_text += "\nстандартное отклонение: " + str(np.std(values))
    report_text += "\nколичество значений выше среднего: " + str(len(values[values > np.mean(values)]))
    report_text += "\n" + "-" * 20 + "\n"

    ax.plot(np.linspace(0, length - 1, length), values, label = path.name)
    ax.set_xlabel("номер")
    ax.set_ylabel("Значение")
    ax.grid(True)
    ax.legend()

report.write_text(report_text, encoding = "utf-8")

fig.savefig(report_directory / "series.png", dpi=150)
plt.show()

