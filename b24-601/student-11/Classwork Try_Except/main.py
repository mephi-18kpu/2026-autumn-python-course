def read_list(l: list):
    try:
        num_of_elem = int(input("Введите размер, задаваемого списка: "))

    except:
        raise TypeError("Не верно введённое число")

    if num_of_elem <= 0:
        raise TypeError("Не верно введённое число")
    
    for i in range(num_of_elem):
        l.append(input("Введите элемент вашего списка: "))

def process_list(l: list):
    try:
        for i in range(len(l)):
            l[i] = float(l[i])//2
    except:
        raise ValueError("Элемент списка не соответствует требованиям")


if __name__ == "__main__":
    my_list = list()

    try:
        read_list(my_list)
        process_list(my_list)
    except TypeError as err:
        print(err)
    except ValueError as err:
        print(err)
    else:
        print(my_list)
