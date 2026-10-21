def stupid_sort(values: list[int]) -> None:
    i=0
    while i < len(values)-1:
        if values[i] > values[i+1]:
            values[i], values[i+1] = values[i+1], values[i]
            i=0
        else:
            i+=1

def chet_nechet_sort(values: list[int]) -> None:
    n = len(values)
    flag=False

    while not flag:
        flag = True
        for i in range(1, n-1, 2):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                flag = False

        for i in range(0, n-1, 2):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                flag = False

def racheska_sort(values: list[int]) -> None:
    n = len(values)
    step = n
    factor = 1.247
    flag = False

    while not flag:
        step = int(step/factor)
        if step <= 1:
            step = 1
            flag = True

        for i in range(0, n-step):
            if values[i] > values[i+step]:
                values[i], values[i+step] = values[i+step], values[i]
                flag = False


def insertion_sort(values: list[int]) -> None:
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1
        while j >= 0 and values[j] > key:
            values[j + 1] = values[j]
            j -= 1

        values[j + 1] = key


def shell_sort(values: list[int]) -> None:
    n = len(values)
    step = n // 2

    while step > 0:
        for i in range(step, n):
            key = values[i]
            j = i

            while j >= step and values[j - step] > key:
                values[j] = values[j - step]
                j -= step

            values[j] = key

        step //= 2

if __name__ == "__main__":
    original = [5, 2, 9, -1, 5, 0, 3]
    print("Исходный список:", original)

    test_1 = original.copy()
    stupid_sort(test_1)
    print("Глупая сортировка:", test_1)

    test_2 = original.copy()
    chet_nechet_sort(test_2)
    print("Чётно-нечётная:", test_2)

    test_3 = original.copy()
    racheska_sort(test_3)
    print("Сортировка расчёской:", test_3)

    test_4 = original.copy()
    insertion_sort(test_4)
    print("Вставками:", test_4)

    test_5 = original.copy()
    shell_sort(test_5)
    print("Шелла:", test_5)
