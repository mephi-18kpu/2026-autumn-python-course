import numpy as np

def moving_average(data: np.typing.NDArray, n: int) -> np.typing.NDArray:
    start_index = 0
    stop_index = n
    mean_values = []

    while stop_index <= len(data):
        mean_values.append(np.sum(data[start_index: stop_index]) /n)
        start_index += 1
        stop_index +=1

    return np.array(mean_values)

if __name__ == "__main__":
    values = np.array([2, 4, 9, 3, 2])
    window_range = 3
    ave_values = moving_average(values, window_range)
    print(ave_values)
