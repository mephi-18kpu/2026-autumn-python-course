import random

def gnome_sort(values: list[int]) -> None:
    index = 0
    n = len(values)

    while index < n:
        if index == 0 or values[index] >= values[index - 1]:
            index += 1
        else:
            values[index], values[index - 1] = values[index - 1], values[index]
            index -= 1

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

tests = {
    "Пустой список": [],
    "Один элемент": [1],
    "Уже отсортирован": [1,2,3,4,5],
    "Обратный порядок": [5,4,3,2,1],
    "Отрицательные числа": [-5, -1, -10, -2, -3, 0],
    "Повторы элементов": [1,2,3,1,4,5],
    "Случайный массив": [random.randint(-50, 50) for _ in range(15)]
}

for name, original_list in tests.items():
    print(f"\nТест: {name}")
    print(f"  Исходный: {original_list}")
    expected = sorted(original_list)

    shaker_test = original_list.copy()
    shaker_sort(shaker_test)
    shaker_ok = (shaker_test == expected)

    gnome_test = original_list.copy()
    gnome_sort(gnome_test)
    gnome_ok = (gnome_test == expected)

    print(f"  Ожидаемый: {expected}")
    print(f"  Shaker Sort: {shaker_test} -> {'Ура, работает' if shaker_ok else 'Не ура, не работает'}")
    print(f"  Gnome Sort:  {gnome_test} -> {'Ура, работает' if gnome_ok else 'Не ура, не работает'}")

    assert shaker_ok, f"Shaker Sort сломался на тесте '{name}'"
    assert gnome_ok, f"Gnome Sort сломался на тесте '{name}'"

print("\n Все тесты успешно пройдены! Обе функции работают корректно.")
