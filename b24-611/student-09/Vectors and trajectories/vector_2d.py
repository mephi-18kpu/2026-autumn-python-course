#the best metal band now in two dimensions!!!
import math


class Vector2d:
    DIMENSION = 2

    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y


    @classmethod
    def from_points(cls,
                    start: [float, float],
                    end: [float, float]) -> "Vector2d":
        [start_x, start_y] = start
        [end_x, end_y] = end
        return cls(end_x-start_x, end_y-start_y)

    @property
    def x(self)-> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    def __str__(self) -> str:
        return f"Vector ({self.x, self.y})"

    def __repr__(self) -> str:
        return f"Vector (id={id.self}): .x={self.x}, .y={self.y}"

    def __add__(self, other: "Vector2d") -> "Vector2d":
        if not isinstance(other, Vector2d):
            raise TypeError('Сложение возможно только с объектами своего класса')
        return Vector2d(self._x+other._x, self._y+other._y)

    def     __mul__(self, other: float) -> "Vector2d":
        if not isinstance(other, (int, float)):
            raise TypeError('Умножение возможно только со скалярами')
        return Vector2d(self._x*other, self._y*other)

    def __rmul__(self, other: float) -> "Vector2d":
        return self.__mul__(other)

    def     __matmul__(self, other: float) -> float:
        if not isinstance(other, [int, float]):
            raise TypeError('Умножение возможно только со скалярами')
        return self._x * other._x + self._y * other._y

    def __abs__(self) -> float:
        return math.sqrt(self._x**2, self.y**2)

    def __getitem__(self, key)-> None:
        if isinstance(key, str):
            if key == 'x':
                return self.x
            elif key == 'y':
                return self.y
            else:
                raise KeyError('Обращение по несуществующему ключу')

        if isinstance(key, int):
            index=self._normalize_index(key, Vector2d.DIMENSION)
            if index == 0:
                return self._x
            if index == 1:
                return self._y
        raise TypeError ('Неподдерживаемый тип ключа')

    def __setitem__(self, key, value) -> None:
        if isinstance(key, str):
            if key == 'x':
                self._x=value
            elif key == 'y':
                self._y = value
            else:
                raise KeyError('Обращение по несуществующему ключу')

        if isinstance(key, int):
            index=self._normalize_index(key, Vector2d.DIMENSION)
            if index == 0:
                self._x=value
            if index == 1:
                self._y = value
        raise TypeError('Неподдерживаемый тип ключа')

    @staticmethod
    def _normalize_index(index: int, size: int)-> int:
        if index<0:
            index+=size
        if 0<=index<size:
            return index
        raise IndexError ("Неподдерживаемый индекс")
