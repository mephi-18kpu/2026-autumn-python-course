def shaker_sort(values: list[int]) -> None:
    if not values:
        return

    left = 0
    right = len(values) - 1

    while left < right:
        swapped = False

        for i in range(left, right):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                swapped = True

        right -= 1

        if not swapped:
            break

        swapped = False

        for i in range(right, left, -1):
            if values[i - 1] > values[i]:
                values[i - 1], values[i] = values[i], values[i - 1]
                swapped = True

        left += 1

        if not swapped:
            break

if __name__ == "__main__":
    test_list = [5, 1, 4, 2, 8, 0, 2, -3]
    print(f"Исходный список: {test_list}")

    shaker_sort(test_list)
    print(f"Отсортированный: {test_list}")
