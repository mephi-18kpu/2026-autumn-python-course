def count_positive(arr: list[float]) -> int:
    cnt = 0
    for i in arr:
        if i > 0.0:
            cnt += 1
    return cnt

measurements = [-2.0, 0.0, 3.5, 7.1]
res = count_positive(measurements)
print(f"Положительных значений: {res}")
