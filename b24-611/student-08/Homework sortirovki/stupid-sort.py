def stupid_sort(arr: list[int]) -> None:
    i = 0
    while i < len(arr) - 1:
        if arr[i] > arr[i + 1]:
            temp = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = temp
            i = 0
        else:
            i += 1


if __name__ == "__main__":
    source = [5, 1, 4, 2, 3]
    expected = sorted(source)
    arr = source.copy()

    stupid_sort(arr)

    print(f"Исходный: {source}")
    print(f"Результат: {arr}")
    print(f"Ожидаемый: {expected}")
    print(f"Верно: {arr == expected}")
