
number = int(input("Введите целое число: "))

if number == 0:
    print("Число 0 является нулём и чётным.")
elif number < 0:
    if number % 2 == 0:
        print(f"Число {number} отрицательное и чётное.")
    else:
        print(f"Число {number} отрицательное и нечётное.")
else:
    if number % 2 == 0:
        print(f"Число {number} положительное и чётное.")
    else:
        print(f"Число {number} положительное и нечётное.")
