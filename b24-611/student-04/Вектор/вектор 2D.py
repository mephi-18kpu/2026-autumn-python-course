import math



class vector_2D:
    DIMENSION = 2


    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    def __setitem__(self, key, value):
        if isinstance(key,str):
            if key == "x":
                self._x = value
                return
            elif key == "y":
                self._y = value
                return
            raise KeyError(f"Попытка получить несуществующее значение по ключу")
        
