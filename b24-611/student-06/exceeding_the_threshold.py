def exceeding_values(values, thershold):
    list_of_exceeding_values=[]
    for value in values:
        if float(value) > thershold:
            list_of_exceeding_values.append(value)
    return list_of_exceeding_values
numbers = (input("Введите числа через пробел ")).split()
porog = float(input("Введите пороговое значение "))

print(exceeding_values(numbers,porog))
