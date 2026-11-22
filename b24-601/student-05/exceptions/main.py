def read_list(l: list[float|int]):
    try:
        length = input('Введите длину списка:')
        if not  length:
            raise TypeError('Во вводе пусто!')
        if '.' in length or ',' in length:
            raise TypeError(f'Число элементов должно быть целым! Введено {length}')
        length = int(length)
        if length < 1:
            raise TypeError(f'Число элементов должно быть положительным! Введено {length}')
    except TypeError as error:
        raise TypeError(f'{error}') from error
    except ValueError:
        raise ValueError('Введено ненатуральное число!')

    for i in range(length):
        try:
            element = input('Введите элемент списка:')
            if not element:
                raise TypeError('Вы не ввели число!')
            if ',' in element:
                raise TypeError('Введите дробь через точку')
            element = float(element)
            l.append(element)
        except TypeError as error:
            raise TypeError(f'{error}') from error
        except ValueError:
            raise ValueError('Элемент списка должен быть числом!')

def process_list(l: list[float|int]):
    try:
        for i in range(len(l)):
            l[i] /= 2
        print(f'Список, поделённый пополам: {l}')
    except ValueError as error:
        raise ValueError(f'{error}') from error

values = []

try:
    read_list(values)
    process_list(values)
except ValueError as error:
   print(error)
except TypeError as error:
    print(error)
