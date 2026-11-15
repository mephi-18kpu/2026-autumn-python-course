def read_list():
    try:
        n = int(input("Введите количество элементов: "))
    except ValueError:
        raise TypeError("Количество элементов должно быть целым числом")

    if n <0:
        raise TypeError("Количество элементов не может быть отрицательным")

    items = []
    for i in range(n):
        items.append(input(f"Элемент {i+1}: "))

    return items


def popolam(items):
    result = []
    for item in items:
        try:
            number = float(item)
        except ValueError:
            raise ValueError(f"Невозможно преобразовать '{item}' в число")

        result.append(number / 2)

    return result


def main():
    try:
        items =read_list()
        halved = popolam(items)
        print("Результат:", halved)
    except ValueError as e:
        print(f"Ошибка: {e}")



if __name__ == "__main__":
    main()
