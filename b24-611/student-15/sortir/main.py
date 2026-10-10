import codHABR
import puzir
import zamer

def main():
    count, minimum_value, maximum_value = codHABR.read_generation_parameters()
    values = codHABR.generative_values(count, minimum_value, maximum_value)
    print(values)
    res, time = zamer.measure_execution_time(puzir.bubble_sort, values)
    puzir.bubble_sort(values)
    print(values)
    print(res, time)
main()

