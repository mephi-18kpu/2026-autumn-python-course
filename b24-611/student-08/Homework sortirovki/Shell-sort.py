def shell_sort(arr: list[int]) -> None:
    step = len(arr) // 2

    while step > 0:
        for i in range(step, len(arr)):
            temp = arr[i]
            j = i

            while j >= step and arr[j - step] > temp:
                arr[j] = arr[j - step]
                j -= step

            arr[j] = temp

        step //= 2


if __name__ == "__main__":
    source = [5, 1, 4, 2, 3, 7, 6]
    expected = sorted(source)
    arr = source.copy()

    shell_sort(arr)

    print(f"Исходный: {source}")
    print(f"Результат: {arr}")
    print(f"Ожидаемый: {expected}")
    print(f"Верно: {arr == expected}")
