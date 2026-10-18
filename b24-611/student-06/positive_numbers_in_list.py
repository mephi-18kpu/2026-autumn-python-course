numbers = (input("Введите числа через пробел ")).split()
positive_numbers = 0
for value in numbers:
    if float(value)>0:
        positive_numbers+=1
print(positive_numbers)
