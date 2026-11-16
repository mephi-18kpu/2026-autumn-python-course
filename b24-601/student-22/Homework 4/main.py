number = int(input("Введите целое число: "))

if number == 0:
    print("Число четное")
else:
    if number < 0:
        print("Число отрицательное")
    else:
        print("Число положительное")

    if number % 2 == 0:
        print("Число четное")
    else:
        print("Число нечетное")