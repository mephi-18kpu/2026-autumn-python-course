#зачем это нужно? Мы создали папку  integration_methods - так называемый пакет.
# Внутри этой папки лежат  файлы с различными методами интегрирования - эти файлы
# называются модулями.
# реализовывать нашу программу мы будем с помощью файла main, и в файле main мы напишем
# import integration_methods. Когда Python увидит эту строку, он залезет в эту папку (пакет)
# и первым делом  откроет именно файл __init__.py
# И всё, что будет описано в __init__.py (например, функции или переменные)
# станет атрибутом пакета integration_methods

from typing import List
from .rectangles import (
    integrate_left_rectangles,
    integrate_midpoint_rectangles,
    integrate_right_rectangles,
)
from .simpson import integrate_simpson # мы импортировали сюда функцию integrate_simpson,
# которая реализует метод интегррования симпсона. Эта функция стала атрибутом пакета
# integration_methods. То есть теперь функция integrate_simpson как бы лежит
# не где-то далеко в файле simpson.py, а прямо тут, среди атрибутов пакета integration_methods
from .trapezoid import integrate_trapezoid # то же самое про метод трапеций
from .type_aliases import Integrand, IntegrationMethod #

# дальше __all__ - это вообщзе очень интересная штука. В итоговом файле main.py мы
# будем импортировать атрибуты пакета integration_methods - те самые функции интегрирования
# если мы захотим импортировать вообще все атрибуты integration_methods - то напишем
# from integration_methods import * - "звёздочка" означает "вообще всё"
# Ключевое слово __all__ означает следующую интсрукцию:
# "Если пользователь попросит тебя импортировать вообще всё содержимое integration_methods
# через звёздочку, то импортируй ему не вообще всё, а только то, что увидишь в списке ниже"

# и вот тут описаны все те функции (атрибуты пакета integration_methods)
# которые надо импортировать
__all__: List[str] = [
    "Integrand",
    "IntegrationMethod",
    "integrate_left_rectangles",
    "integrate_midpoint_rectangles",
    "integrate_right_rectangles",
    "integrate_trapezoid",
    "integrate_simpson",
]
