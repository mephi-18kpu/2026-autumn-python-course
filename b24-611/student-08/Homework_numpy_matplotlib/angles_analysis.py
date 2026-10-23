from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

base_dir = Path(__file__).resolve().parent
data_dir = base_dir / "data" / "angles"
res_dir = base_dir / "results"
ang_res_dir = res_dir / "angles"
ang_res_dir.mkdir(parents=True, exist_ok=True)

files = []
for f in data_dir.iterdir():
    if f.is_file() and f.suffix == ".txt":
        files.append(f)
files = sorted(files)

report = ""
max_cnt = -1
max_cnt_file = ""

x_plot = np.linspace(0, 180, 181)
y_sin_plot = np.sin(np.deg2rad(x_plot))
y_cos_plot = np.cos(np.deg2rad(x_plot))

for f in files:
    arr = np.loadtxt(f)
    rad = np.deg2rad(arr)
    s = np.sin(rad)
    c = np.cos(rad)

    stem = f.stem
    np.savetxt(ang_res_dir / f"{stem}_sin.txt", s)
    np.savetxt(ang_res_dir / f"{stem}_cos.txt", c)

    mx_ang = np.max(arr)
    cnt = np.count_nonzero(s > 0.6)

    if cnt > max_cnt:
        max_cnt = cnt
        max_cnt_file = f.name

    report += f"Файл: {f.name}\n"
    report += f"Максимальный угол: {mx_ang}\n"
    report += f"Углов с sin > 0.6: {cnt}\n\n"

    fig, ax = plt.subplots()
    ax.plot(x_plot, y_sin_plot, label="Синус")
    ax.plot(x_plot, y_cos_plot, label="Косинус")
    ax.scatter(arr, s, color="red", label="Точки синуса")
    ax.scatter(arr, c, color="orange", label="Точки косинуса")
    ax.set_xlabel("Угол, градусы")
    ax.set_ylabel("Значение")
    ax.set_title(f"Анализ {f.name}")
    ax.grid(True)
    ax.legend()

    fig.savefig(ang_res_dir / f"{stem}.png")
    plt.show()

report += f"Больше всего углов с sin > 0.6 в файле: {max_cnt_file}\n"

with open(res_dir / "angles_report.txt", "w", encoding="utf-8") as f_out:
    f_out.write(report)
