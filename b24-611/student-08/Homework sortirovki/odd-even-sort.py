def odd_even_sort(arr: list[int]) -> None:
    flag = False
    while not flag:
        flag = True

        for i in range(1, len(arr) - 1, 2):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                flag = False

        for i in range(0, len(arr) - 1, 2):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                flag = False


if __name__ == "__main__":
    source = [5, 1, 4, 2, 3, 7, 6]
    expected = sorted(source)
    arr = source.copy()

    odd_even_sort(arr)

    print(f"Исходный: {source}")
    print(f"Результат: {arr}")
    print(f"Ожидаемый: {expected}")
    print(f"Верно: {arr == expected}")
