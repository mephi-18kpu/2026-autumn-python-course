def process_list(items):

    try:
        halves = [item / 2 for item in items]
    except TypeError:
        print("элементы списка - чиселки")
        return

    print("\nРезультат:")
    for i, value in enumerate(halves, start=1):
        print(f"{i}) {float(value)}")


def main():

    try:
        n = int(input("Kolichestvo elementov: у"))
    except ValueError:
        print("необходимо цело число")
        return

    if n < 0:
        print("не отрицательное")
        return

    items = []
    for i in range(n):
        try:
            value = float(input(f"Введите element {i + 1}: "))
        except ValueError:
            print(f"вводи чиселки")
            return
        items.append(value)

    process_list(items)


if __name__ == "__main__":
    main()
