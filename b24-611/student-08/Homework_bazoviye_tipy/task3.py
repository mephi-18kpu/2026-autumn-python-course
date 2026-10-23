def count_codes(arr: list[int]) -> dict[int, int]:
    d = {}
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

error_codes = [101, 205, 101, 404, 205, 101]
res = count_codes(error_codes)
print(res)
