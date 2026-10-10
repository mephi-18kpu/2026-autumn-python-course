def select_high_measurements(measurements: [float], threshold: float) -> [float]:
    high_values = []
    for measurement in measurements:
        if measurement > threshold:
            high_values.append(measurement)
    return high_values
measurements = [12.5, 31.0, 28.4, 35.2]
high_measurements = select_high_measurements(measurements, 30.0)
print(high_measurements)
