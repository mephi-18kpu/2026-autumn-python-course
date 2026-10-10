from generation import generate_values
import sorted_function

list = generate_values(10, 10, 35)
print(*list)
bubble_sort(list)
print(*list)


