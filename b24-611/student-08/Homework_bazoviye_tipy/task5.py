first_values = [1, 2]
second_values = first_values.copy()

second_values.append(3)

print(first_values)
print(second_values)


#python в исходной программе не создавал нового списка, и second_values это было второе название исходного, следовательно меняли исходный
