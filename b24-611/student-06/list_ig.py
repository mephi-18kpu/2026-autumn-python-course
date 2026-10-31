#В исходной версии обе переменные (first_values и second_values) ссылаются на один и тот же объект list.
#Поэтому добавление элемента через second_values изменяет список, доступный через обе переменные.
#Чтобы избежать этого, нужно воспользоваться copy
first_values = [1, 2]
second_values = first_values.copy()

second_values.append(3)

print(first_values)
print(second_values)
