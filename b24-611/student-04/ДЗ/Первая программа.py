number = int(input("Введите целое число: "))

if number == 0:
    print("Число равно нулю.")
elif number < 0:
    print("Число отрицательное.")
else:
    print("Число положительное.")

# Проверка чётности
if number % 2 == 0:
    print("Число чётное.")
else:
    print("Число нечётное.")
