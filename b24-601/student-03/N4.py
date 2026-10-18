
sensor_names = ["температура","давление","температура","скорость","давление",]
unic_sensor_names=set(sensor_names)
print(unic_sensor_names)
print(f"Количество уникальных датчиков:{len(unic_sensor_names)}")