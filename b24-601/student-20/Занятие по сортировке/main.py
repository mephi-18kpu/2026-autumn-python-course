"""Содержит примеры для занятия о сортировке и поиске."""
# System imports

# External imports

# User imports
from generate import read_generation_parameters
from generate import generate_values
from generate import measure_execution_time
from sort import bubble_sort

#############################################

def main() -> None:
    parameters = read_generation_parameters()
    generated_list = generate_values(parameters[0], parameters[1], parameters[2])
    bubble_sort(generated_list)
    print(generated_list)
    time_parameters = measure_execution_time(bubble_sort, generated_list)
    print(time_parameters)

if __name__ == "__main__":
    main()
