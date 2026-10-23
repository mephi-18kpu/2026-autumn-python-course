def insertion_sort(arr: list[int]) -> None:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


if __name__ == "__main__":
    source = [5, 1, 4, 2, 3, 7, 6]
    expected = sorted(source)
    arr = source.copy()

    insertion_sort(arr)

    print(f"Исходный: {source}")
    print(f"Результат: {arr}")
    print(f"Ожидаемый: {expected}")
    print(f"Верно: {arr == expected}")
