def gnome_sort(znacheniya: list[int]) -> None:
    indeks = 0

    while indeks < len(znacheniya):
        if indeks == 0 or znacheniya[indeks] >= znacheniya[indeks - 1]:
            indeks = indeks + 1
        else:
            znacheniya[indeks], znacheniya[indeks - 1] = znacheniya[indeks - 1], znacheniya[indeks]
            indeks = indeks - 1


if __name__ == "__main__":
    spisok = [4, 1, 3, 2, 7, -1, 4]
    print(f"Исходный список: {spisok}")
    gnome_sort(spisok)
    print(f"Отсортированный список: {spisok}")
