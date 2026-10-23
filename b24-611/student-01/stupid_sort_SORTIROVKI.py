def stupid_sort(znacheniya: list[int]) -> None:
    indeks = 0

    while indeks < len(znacheniya) - 1:
        if znacheniya[indeks] > znacheniya[indeks + 1]:
            znacheniya[indeks], znacheniya[indeks + 1] = znacheniya[indeks + 1], znacheniya[indeks]
            indeks = 0
        else:
            indeks = indeks + 1


if __name__ == "__main__":
    spisok = [3, 1, 4, 1, 5]
    print(f"Исходный список: {spisok}")
    stupid_sort(spisok)
    print(f"Отсортированный список: {spisok}")
