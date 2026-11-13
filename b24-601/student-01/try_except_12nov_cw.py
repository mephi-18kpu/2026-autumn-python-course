def read_list(l: list):
    while True:
        try:
            n = int(input("Введите длину списка: "))
            if n <= 0:
                print("Длина списка должна быть положительной, введите еще раз")
                continue
            break
        except ValueError:
            print("Длина списка должна быть целым числом, введите еще раз")

    for num in range(n):
        while True:
            try:
                number = int(input(f"Введите число {num+1}: \t"))
                if number < 0:
                    raise ValueError(f"Число {num+1} должно быть положительным, введите еще раз")

                l.append(number)
                break

            except ValueError:
                print(f"Число {num + 1} должно быть целым, введите еще раз")


# def process_list1(l: list):
#     for i in range(len(l)):
#         if l[i] % 2 != 0:
#             raise ValueError(f"Число {l[i]} не делится на 2 нацело")
#         l[i] = l[i] // 2

def process_list2(l: list):
    for i in range(len(l)):
        l[i] = l[i] / 2

values = []
try:
    read_list(values)

    # process_list1(values)
    # print(*values, sep="\t")

    process_list2(values)
    print(*values, sep="\t")


except ValueError as e1:
    print(f"Ошибка значения: {e1}")
except TypeError as e2:
    print(f"Ошибка типа: {e2}")
