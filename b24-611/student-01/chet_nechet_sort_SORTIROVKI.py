def odd_even_sort(znacheniya: list[int]) -> None:
    otsortirovano = False

    while not otsortirovano:
        otsortirovano = True

        for i in range(1, len(znacheniya) - 1, 2):
            if znacheniya[i] > znacheniya[i + 1]:
                znacheniya[i], znacheniya[i + 1] = znacheniya[i + 1], znacheniya[i]
                otsortirovano = False

        for i in range(0, len(znacheniya) - 1, 2):
            if znacheniya[i] > znacheniya[i + 1]:
                znacheniya[i], znacheniya[i + 1] = znacheniya[i + 1], znacheniya[i]
                otsortirovano = False


if __name__ == "__main__":
    spisok = [8, 5, 2, 9, 1, 6, 3]
    print(f"Исходный список: {spisok}")
    odd_even_sort(spisok)
    print(f"Отсортированный список: {spisok}")
