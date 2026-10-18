sensor_names = (input("Введите названия датчиков через пробел: ")).split()

unique_sensor_names = set(sensor_names)

print(unique_sensor_names)
print(f"Количество различных датчиков: {len(unique_sensor_names)}")
