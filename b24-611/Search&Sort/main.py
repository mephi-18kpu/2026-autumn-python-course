#System imports
import time
from collections.abc import Callable

#External imports
import list_creator
import bubble_sort
#User imports

##########################
def measure_execution_time(
    function: Callable[..., object],
    *args: object,
) -> tuple[object, float]:
    start_time=time.time()
    result=function(*args)
    stop_time=time.time()
    return result, stop_time-start_time

def main():
    count, minimum_value, maximum_value = list_creator.read_generation_parameters()
    values = list_creator.generate_values(count, minimum_value, maximum_value)
    print(values)
    res, time = measure_execution_time(bubble_sort.bubble_sort, values)
    print(values)
    print(res, time)

main()
