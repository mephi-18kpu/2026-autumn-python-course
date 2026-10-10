from generation import read_generation_parameters, generate_values
from sort import bubble_sort
def main():
    parameters = read_generation_parameters()
    output = generate_values(parameters[0],parameters[1],parameters[2])
    print(output)
    bubble_sort(output)
    print(output)
    return 0
main()
