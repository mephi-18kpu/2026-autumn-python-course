def count_of_positive_numbers(values):
    positive_numbers=0
    for value in values:
        if float(value) > 0:
            positive_numbers += 1
    return positive_numbers
numbers = (input("Введите числа через пробел ")).split()

print(count_of_positive_numbers(numbers))
