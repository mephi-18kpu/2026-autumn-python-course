def rolling_mean(values: list(float), w: int) -> list[float]:
    filtered_values = []
    for i in range(len(values) - w + 1):
        filtered_values.append(sum(values[i: i + w ]) / w)

    return filtered_values


if __name__ == "__main__":
    data = [2,4,9,3,2]
    filtered_data = rolling_mean(data,3)
    print(filtered_data)
