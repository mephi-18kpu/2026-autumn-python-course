measurements = list(map(float, input().split()))
def positive_integer(measurements: list[float]) -> list[float]:
    count = 0
    for measurement in measurements:
        if measurement > 0:
            count += 1


    return count
print(positive_integer(measurements))

list_count = list(map(float, input().split()))
threshold = int(input())
def threshhold_numbers(list_count: list[float]) -> list[float]:
    undthreshhold = []
    for i in list_count:
        if i > threshold:
            undthreshhold.append(i)

    return undthreshhold
print(threshhold_numbers(list_count))
