"""Получение множества уникальных названий датчиков."""

raw_sensor_names = input(
    "Введите названия датчиков через запятую: "
)
sensor_names = [name.strip() for name in raw_sensor_names.split(",")]

unique_sensor_names = set(sensor_names)

print(f"Уникальные датчики: {unique_sensor_names}")
print(f"Количество различных датчиков: {len(unique_sensor_names)}")
