## глупая, четно-нечетная сортировка, расческа, вставки, Шелла. душнилово лютое

def stupid_sort(values: list[int]) -> None:
    index = 0
    while index < len(values) - 1:
        if values[index] > values[index + 1]:
            values[index], values[index + 1] = values[index + 1], values[index]
            index = 0
        else: index += 1


def chet_nechet(values: list[int]) -> None:
    flag = False
    length = len(values)
    while not flag:
        flag = True

        for i in range(1, length-1, 2):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                flag = False

        for i in range(0, length-1, 2):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                flag = False


def rascheska(values: list[int]) -> None:
    length = len(values)
    gap = length
    shrink_factor = 1.2473
    flag = False
    while not flag:
        gap = int(gap/shrink_factor)
        if gap<= 1:
            gap = 1
            flag = True
        ind = 0
        while ind + gap < length:
            if values[ind] > values[ind + gap]:
                values[ind], values[ind + gap] = values[ind + gap], values[ind]
                flag = False
            ind += 1


def insertion_sort(values: list[int]) -> None:
    for i in range(1, len(values)):
        current_value = values[i]
        position = i - 1
        while position >= 0 and values[position] > current_value:
            values[position + 1] = values[position]
            position -= 1
        values[position + 1] = current_value


def shell_sort(values: list[int]) -> None:
    length = len(values)
    gap = length//2
    while gap > 0:
        for index in range(gap, length):
            current_value = values[index]
            position = index
            while position >= gap and values[position - gap] > current_value:
                values[position] = values[position - gap]
                position -= gap
            values[position] = current_value
        gap //= 2


for name, func in [
    ("Глупи", stupid_sort),
    ("Ч/Н", chet_nechet),
    ("Расческа", rascheska),
    ("Вставки", insertion_sort),
    ("Шелла", shell_sort),
]:
    data = [4, 1, 4, 2, 1, 3, 2]
    # data2 = [4, 1, 4, 2, 1, 3, 2, 45, 69, -67, 1488]
    func(data)
    # func(data2)
    print(name, data == sorted([4, 1, 4, 2, 1, 3, 2]))
print("--------------")

for name, func in [
    ("Глупи", stupid_sort),
    ("Ч/Н", chet_nechet),
    ("Расческа", rascheska),
    ("Вставки", insertion_sort),
    ("Шелла", shell_sort),
]:
    data2 = [4, 1, 4, 2, 1, 3, 2, 45, 69, -67, 1488]
    func(data2)
    print(name, data2 == sorted([4, 1, 4, 2, 1, 3, 2, 45, 69, -67, 1488]))
print(sorted([4, 1, 4, 2, 1, 3, 2, 45, 69, -67, 1488]))
print("end")








