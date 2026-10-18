
number = int(input("Введите целое число: "))

if number == 0:
    print("Число равно нулю")
elif number % 2 == 0:
    print("Число чётное")
else:
    print("Число нечётное")

if number > 0:
    print("Число положительное")
elif number < 0:
    print("Число отрицательное")
