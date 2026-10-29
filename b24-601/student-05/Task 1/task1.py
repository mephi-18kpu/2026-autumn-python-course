def count_positive_measurements(measurements: [float]) -> int:
    positive = 0
    for measurement in measurements:
        if measurement > 0:
            positive += 1
    return positive
measurements = [2.0, 0.0, 3.5, 7.1]
positive_count = count_positive_measurements(measurements)

