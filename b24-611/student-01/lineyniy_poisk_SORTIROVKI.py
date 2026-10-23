def linear_search(znacheniya: list[int], tsel: int) -> int | None:
    for indeks, znachenie in enumerate(znacheniya):
        if znachenie == tsel:
            return indeks
    return None


if __name__ == "__main__":
    spisok = [10, 25, 3, 8, 25, 1]
    iskomoe_chislo = 25
    print(f"Список: {spisok}")
    print(f"Ищем число: {iskomoe_chislo}")
    rezultat = linear_search(spisok, iskomoe_chislo)
    print(f"Индекс найденного элемента: {rezultat}")
