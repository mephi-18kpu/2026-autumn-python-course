def binary_search(znacheniya: list[int], tsel: int) -> int | None:
    levyy_indeks = 0
    pravyy_indeks = len(znacheniya) - 1

    while levyy_indeks <= pravyy_indeks:
        sredniy_indeks = (levyy_indeks + pravyy_indeks) // 2
        srednee_znachenie = znacheniya[sredniy_indeks]

        if srednee_znachenie == tsel:
            return sredniy_indeks

        if srednee_znachenie < tsel:
            levyy_indeks = sredniy_indeks + 1
        else:
            pravyy_indeks = sredniy_indeks - 1

    return None


if __name__ == "__main__":
    otsortirovannyy_spisok = [1, 3, 5, 7, 9, 11, 13, 15]
    iskomoe_chislo = 9
    print(f"Отсортированный список: {otsortirovannyy_spisok}")
    print(f"Ищем число: {iskomoe_chislo}")
    rezultat = binary_search(otsortirovannyy_spisok, iskomoe_chislo)
    print(f"Индекс найденного элемента: {rezultat}")
