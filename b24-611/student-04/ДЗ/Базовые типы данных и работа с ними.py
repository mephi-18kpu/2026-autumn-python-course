def count_positive_measurements(measurements):
    a = 0
    for measurement in measurements:
        if measurement > 0:
            a += 1
    return a

print(count_positive_measurements([1, 2, 3, 4, -5, 6, 7, -8, 9, 10]))



def select_high_measurements(measurements, threshold):
    l = []
    for measurement in measurements:
        if measurement > threshold:
            l.append(measurement)
    return l

print(select_high_measurements([1, 2, 3, 4, -5, 6, 7, -8, 9, 10],5))



def count_error_codes(error_codes: list[int]) -> dict[int, int]:
    error_counts = {}
    for error_code in error_codes:
        if error_code in error_counts:
            error_counts[error_code] += 1
        else:
            error_counts[error_code] = 1
    return error_counts

error_codes = [101, 205, 101, 404, 205, 101]
print(count_error_codes(error_codes))



sensor_names = [
    "температура",
    "давление",
    "температура",
    "скорость",
    "давление",
]

unique_sensor_names = set(sensor_names)
print(unique_sensor_names)
print(f"Количество различных датчиков: {len(unique_sensor_names)}")



first_values = [1, 2]        # (1) создан список, имя first_values ссылается на него
second_values = first_values # (2) второе имя ссылается на ТОТ ЖЕ список
second_values.append(3)      # (3) изменяем список через второе имя
print(first_values)          # (4) видим изменение через первое имя

#Присваивание second_values = first_values не копирует список — оно просто создаёт второе имя для того же самого объекта в памяти. append(3) меняет сам объект-список, а не имя. Поэтому изменение видно через оба имени — они ведь указывают на один и тот же список.

first_values = [1, 2]
second_values = first_values.copy()   # создаётся новый список
second_values.append(3)

print(first_values)
print(second_values)
