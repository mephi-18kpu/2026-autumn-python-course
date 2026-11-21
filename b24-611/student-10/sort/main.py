from generation import *
from bubble_sort import bubble_sort
from sort_timer import *
def main():
    ...
    print("начало сортитровки\n")

    count, min_val, max_val = read_generation_parameters()

    list = generate_values(count, min_val, max_val)

    print(f"исходный список: {list}\n")

    result, execution_time = measure_execution_time(bubble_sort(list))

    print(f"отсртированный список: {list}\n")
    print(f"время сортировки: {execution_time}\n, сек")

main()
