"""Демонстрация общей ссылки на список и создания копии."""

raw_values = input("Введите элементы списка через пробел: ")
first_values = [int(value) for value in raw_values.split()]

# Присваивание не создаёт копию: обе переменные ссылаются на один список.
second_values = first_values
second_values.append(3)

print("После изменения общего списка:")
print(f"first_values: {first_values}")
print(f"second_values: {second_values}")

# Создаём независимую копию исходного списка.
first_values = [int(value) for value in raw_values.split()]
second_values = first_values.copy()
second_values.append(3)

print("После изменения копии:")
print(f"first_values: {first_values}")
print(f"second_values: {second_values}")
