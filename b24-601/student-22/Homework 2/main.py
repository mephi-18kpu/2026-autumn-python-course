def count_positive_measurements(measurements):
    count = 0
    for num in measurements:
        if num > 0:
            count = count + 1
    return count


measurements_1 = [-2.0, 0.0, 3.5, 7.1]
positive_count = count_positive_measurements(measurements_1)
print("№1 результат:", positive_count)


def select_high_measurements(measurements, threshold):
    high_list = []
    for num in measurements:
        if num > threshold:
            high_list.append(num)
    return high_list


measurements_2 = [12.5, 31.0, 28.4, 35.2]
high_measurements = select_high_measurements(measurements_2, 30.0)
print("№2 результат:", high_measurements)



error_codes = [101, 205, 101, 404, 205, 101]

error_dict = {}

for code in error_codes:
    if code in error_dict:
        error_dict[code] = error_dict[code] + 1
    else:
        error_dict[code] = 1

print("№3 результат:", error_dict)


sensor_names = [
    "температура",
    "давление",
    "температура",
    "скорость",
    "давление",
]

unique_sensors = set(sensor_names)
print("№4 множество:", unique_sensors)

count_sensors = len(unique_sensors)
print("№4 количество разных датчиков:", count_sensors)



first_values = [1, 2]
second_values = first_values.copy()
second_values.append(3)

print("first_values:", first_values)
print("second_values:", second_values)












