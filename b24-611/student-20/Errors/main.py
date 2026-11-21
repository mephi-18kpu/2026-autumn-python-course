def create_list (l: list):
    count=input("Введите количество элементов")
    for i in range(int(count)):
        elem=input("Введите элементы")
        l.append(elem)
    return l
def process_list(l: list):
    li=create_list(l)
    li2=[]
    for i in range(len(l)):
        li[i]=int(li[i])
        li2.append(li[i]/2)
    return li2

values=[]
try:
    process_list(values)
except ValueError as error:
    print(f"Введите целые числа в список: ({error})")
except TypeError as error:
    print(f"Операция не может быть выполнена:({error})")
