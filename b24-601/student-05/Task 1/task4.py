def uniqe_sensor_counter(sensors: [str]) -> dict[str, int]:
    uniqe_sensors = {}
    for sensor in sensors:
        if sensor in uniqe_sensors:
            uniqe_sensors[sensor] += 1
        else:
            uniqe_sensors[sensor] = 1
    return uniqe_sensors
sensor_names = [
    "температура",
    "давление",
    "температура",
    "скорость",
    "давление",
]
print(uniqe_sensor_counter(sensor_names))

