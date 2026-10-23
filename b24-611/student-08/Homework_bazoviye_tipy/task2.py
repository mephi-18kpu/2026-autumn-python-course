def select_high(arr: list[float], thresh: float) -> list[float]:
    res = []
    for i in arr:
        if i > thresh:
            res.append(i)
    return res

measurements = [12.5, 31.0, 28.4, 35.2]
high = select_high(measurements, 30.0)
print(f"Значения выше порога: {high}")
