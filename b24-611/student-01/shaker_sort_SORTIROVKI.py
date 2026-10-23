def shaker_sort(znacheniya: list[int]) -> None:
    levyy_indeks = 0
    pravyy_indeks = len(znacheniya) - 1
    obmen_byl = True

    while obmen_byl and levyy_indeks < pravyy_indeks:
        obmen_byl = False
        for i in range(levyy_indeks, pravyy_indeks):
            if znacheniya[i] > znacheniya[i + 1]:
                znacheniya[i], znacheniya[i + 1] = znacheniya[i + 1], znacheniya[i]
                obmen_byl = True

        pravyy_indeks = pravyy_indeks - 1

        if not obmen_byl:
            break

        obmen_byl = False
        for i in range(pravyy_indeks, levyy_indeks, -1):
            if znacheniya[i - 1] > znacheniya[i]:
                znacheniya[i - 1], znacheniya[i] = znacheniya[i], znacheniya[i - 1]
                obmen_byl = True

        levyy_indeks = levyy_indeks + 1


if __name__ == "__main__":
    spisok = [5, 2, 9, 1, 5, 6, -3, 0]
    print(f"Исходный список: {spisok}")
    shaker_sort(spisok)
    print(f"Отсортированный список: {spisok}")
