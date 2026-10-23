def shell_sort(znacheniya: list[int]) -> None:
    dlina = len(znacheniya)
    shag = dlina // 2

    while shag > 0:
        for i in range(shag, dlina):
            vremennoe_znachenie = znacheniya[i]
            j = i

            while j >= shag and znacheniya[j - shag] > vremennoe_znachenie:
                znacheniya[j] = znacheniya[j - shag]
                j = j - shag

            znacheniya[j] = vremennoe_znachenie

        shag = shag // 2


if __name__ == "__main__":
    spisok = [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
    print(f"Исходный список: {spisok}")
    shell_sort(spisok)
    print(f"Отсортированный список: {spisok}")
