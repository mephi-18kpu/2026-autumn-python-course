# System imports
from pathlib import Path
# External imports
import matplotlib.pyplot as plt
import numpy as np

# User imports

#############################################

script_directory = Path(__file__).resolve().parent.parent
data_directory = script_directory / "data" / "angles"

results_directory = data_directory / "results"
results_directory.mkdir(exist_ok=True)
report = results_directory / "angles_report.txt"

report_text = ""

for path in data_directory.iterdir():
    if path.name == "README.md" or path.name == "results":
        continue

    values = np.loadtxt(path)
    rad = np.deg2rad(values)
    name = path.stem
    sinus = results_directory / (name + "_sin.txt")
    cosinus = results_directory / (name + "_cos.txt")

    length = len(rad)

    np.savetxt(results_directory / sinus, np.sin(rad) , fmt="%.1f")
    np.savetxt(results_directory / cosinus, np.cos(rad), fmt="%.1f")

    report_text += str(path.name)
    report_text += "\nмаксимум: " + str(np.max(values))
    report_text += "\nчисло значений синуса строго больше 0.6: " + str(len(values[np.sin(values) > 0.6]))
    report_text += "\n" + "-" * 20 + "\n"

    angles = np.linspace(-90, 360, 451)
    radians = np.deg2rad(angles)

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(angles, np.cos(radians), label="Косинус", color="tab:green")
    ax.plot(angles, np.sin(radians), label="Синус", color="tab:red")

    ax.scatter(values, np.cos(rad), color="tab:orange")
    ax.scatter(values, np.sin(rad), color="tab:orange")

    ax.set_xlabel("angles")
    ax.set_ylabel("sinus, cosinus")
    ax.grid(True)
    ax.legend()
    fig.savefig(results_directory / (name + ".png"), dpi=150)
    plt.show()

report.write_text(report_text, encoding = "utf-8")


