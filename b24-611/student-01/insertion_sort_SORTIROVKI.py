def insertion_sort(znacheniya: list[int]) -> None:
    for i in range(1, len(znacheniya)):
        klyuch = znacheniya[i]
        j = i - 1

        while j >= 0 and znacheniya[j] > klyuch:
            znacheniya[j + 1] = znacheniya[j]
            j = j - 1

        znacheniya[j + 1] = klyuch


if __name__ == "__main__":
    spisok = [12, 11, 13, 5, 6, -2, 0]
    print(f"Исходный список: {spisok}")
    insertion_sort(spisok)
    print(f"Отсортированный список: {spisok}")
