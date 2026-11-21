import math

class Vector2d:
    DIMENSION = 2

    def __init__(self, x: float|int, y: float|int):
        self._x = x
        self._y = y

    @classmethod
    def from_points(cls,
                    start: tuple[float|int, float|int],
                    end: tuple[float|int, float|int],
                    ) -> "Vector2d":

        start_x, start_y = start
        end_x, end_y = end

        return cls(end_x - start_x, end_y - start_y)

    @property
    def x(self) -> float|int:
        return self._x

    @property
    def y(self) -> float|int:
        return self._y

    def __getitem__(self, key) -> float|int:
        if isinstance(key, str):
            if key == "x":
                return self._x
            if key == "y":
                return self._y
            raise KeyError(f"У типа вектор есть только поля x и y.\n"
                           f"Попытка получить значения поля {key}")

    def __setitem__(self, key, value):
        if key == "x":
             self._x = value
        if key == "y":
             self._y = value

    def __repr__(self) -> str:
        return f"Vector2d id = ({id(self)}) with ._x = {self.x} ._y = {self.y}"

    def __add__(self, other: "Vector2d") -> "Vector2d":
        if not isinstance(other, Vector2d):
            raise TypeError (f"Сложение вектора возможно только с другим вектором")
        return Vector2d(self._x + other._x, self._y + other._y)

    def __mul__(self, scalar: float|int ) -> "Vector2d":
        if not isinstance(scalar, Vector2d):
            raise TypeError (f"Умножение вектора возможно только на float|int")
        return Vector2d(self._x * scalar, self._y * scalar)

    def __rmul__(self, scalar: float|int) -> "Vector2d":
        return self.__mul__(scalar)

    def __abs__(self) -> float|int:
        return math.sqrt(self._x**2 + self._y**2)

    def __matmul__(self, other: "Vector2d" ):
        if not isinstance(other, Vector2d):
            raise TypeError(f"Математическое умножение вектора возможно только на вектор")
        return self.x * other.y + self.x * other.y

    def dot(self, other: "Vector2d") -> float|int:
        return self.__matmul__(other)


    @staticmethod
    def _normalize_index(index: int, size: int):
        if index < 0:
            index += 2
        if index < 0 or index >= size:
            raise IndexError("Индекс компоненты вне диапазона!")
        return index
