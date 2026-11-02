from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

p = Path('C:/Users/ASUS/Desktop/Python/2026-autumn-python-course/code-examples/NumPy и Matplotlib/data/series')

text_files = [
    item for item in p.iterdir()
    if item.is_file() and item.suffix == ".txt"
]

files_len = []
files_max = []
files_min = []
files_mean = []
files_std = []
files_cnt_big_nums = []

for i in text_files:
    array = np.loadtxt(i)
    files_len.append(len(array))
    files_max.append(array.max().item())
    files_min.append(array.min().item())
    files_mean.append(array.mean().item())
    files_std.append(array.std().item())
    files_cnt_big_nums.append((array > array.mean()).sum().item())

max_index_mean = files_mean.index(max(files_mean))
min_index_std = files_std.index(min(files_std))

out_file = Path("result") / "series_report.txt"
out_file.parent.mkdir(parents=True, exist_ok=True)

lines = []
for file, flen, fmax, fmin, mn, std, cnt in zip(
    text_files, files_len, files_max, files_min, files_mean,
    files_std, files_cnt_big_nums):
    lines.append(
        f"{file.name}: length={flen}, max={fmax:.2f}, min={fmin:.2f}, "
        f"mean={mn:.2f}, std={std:.2f}, above_mean={cnt}"
    )

lines.append(f"Max mean value has {text_files[max_index_mean].name}:"
             f" {files_mean[max_index_mean]}\n"
             f"And min standard value has {text_files[min_index_std].name}"
             f" {files_std[min_index_std]}")
out_file.write_text("\n".join(lines), encoding="utf-8")

fig, ax = plt.subplots(1, 1, figsize=(16, 9))
ax.grid(True, alpha=0.6)
ax.set_title("Распределение точек")
ax.set_xlabel("Порядковый номер, N")
ax.set_ylabel("Значение числа, y")
files_name= []

for i in range(len(text_files)):
    array = np.loadtxt(text_files[i])
    ar = np.arange(0, len(array))
    ax.plot(ar, array, marker="o")
    files_name.append(text_files[i].name)

ax.legend(files_name)
plt.savefig(Path("result") / "series.png")
plt.show()
