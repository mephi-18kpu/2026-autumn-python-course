
def select_high_measurements(measurements: list, a:int):
    high_measurements = list()
    for measurement in measurements:
        if measurement >= a:
            high_measurements.append(measurement)
    return high_measurements

measurements = [12.5, 31.0, 28.4, 35.2]
x = int(input())
print(select_high_measurements(measurements, x))
print(high_measurements)