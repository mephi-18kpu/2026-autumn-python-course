def comb_sort(arr: list[int]) -> None:
    step = len(arr)
    flag = True

    while step > 1 or flag:
        step = int(step / 1.247)
        if step < 1:
            step = 1

        flag = False

        for i in range(len(arr) - step):
            if arr[i] > arr[i + step]:
                temp = arr[i]
                arr[i] = arr[i + step]
                arr[i + step] = temp
                flag = True


if __name__ == "__main__":
    source = [5, 1, 4, 2, 3, 7, 6]
    expected = sorted(source)
    arr = source.copy()

    comb_sort(arr)

    print(f"Исходный: {source}")
    print(f"Результат: {arr}")
    print(f"Ожидаемый: {expected}")
    print(f"Верно: {arr == expected}")
