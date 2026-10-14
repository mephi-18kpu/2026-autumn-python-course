import time
from collections.abc import Callable

def measure_execution(
    function: Callable[..., object],
    *args: object,
) -> tuple[object, float]:

    start_time = time.time()
    result = function(*args)
    stop_time = time.time()

    return result, stop_time - start_time
