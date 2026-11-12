def read_list(l: list):
    try:
        amount_of_values = int(input("Введите количество элементов: "))
        if amount_of_values < 0:
            raise ValueError
    except ValueError:
        raise TypeError("неправильно: нужно ввести положительное целое число")

    for i in range(amount_of_values):
        item = input(f"Введите элемент {i + 1}: ")
        l.append(item)
    return l


def process_list(l: list):
    for i in range(len(l)):
        try:
            l[i] = int(l[i]) / 2
        except ValueError:
            raise TypeError(f"неправильно: элемент '{l[i]}' не является числом")
    return l


values = []

try:
    print("Исходный список:", read_list(values))
    print("Обработанный список:", process_list(values))
except TypeError as error:
    print(f"Ошибка: {error}")
