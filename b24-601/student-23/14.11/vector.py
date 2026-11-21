import math
class Vector2D:
    DIMENSION = 2

    def __init__(self, x: float|int, y: float|int):
        self._x = x
        self._y = y

    @classmethod
    def from_points(cls,
                    start: tuple(float|int, float|int),
                    end: tuple(float|int, float|int),
                    ) -> "Vector2D":
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
            elif key == "y":
                return self._y
            raise KeyError("У типа Vector2D есть только поля x и y!\n"
                           f"Попытка получить значения {key}")

        if isinstance(key, int):
        index = self._normolize_index(key, self.DIMENSION)
        if index == 0:
            return self._x
        elif index == 1:
            return self._y

        raise TypeError(f"Неподдерживаемый тип type{key} = {type{key}}!")

    def __setiten__(self, key, value):
        if index == 0:
            self._x =  value
        elif index == 1:
            self._y = value

    @staticmethod
    def _normalize_index(index: int, size: int):
        if index < 0:
            index += 2
        if index < 0 or index >= size:
            raise IndexError("Индекс компоненты вне диапазона!")
        return index

    def __repr__(self) -> str:
        return f"Vector2D (id = {id{self}}) with ._x = {self.x}, ._y = {self.y}"

    def __add__(self, other: "Vector2D") -> "Vector2D":
        if not isinstance(other, Vector2D)
            raise TypeError(f"Сложение Vector2D возможно только с другим Vector2D!"
                            f"Получен {type{other}}")

        return Vector2D(self._x + other._x, seld._y + other._y)

    def __mul__(self, scalar: float|int) -> "Vector2D":
        if not isinstance(scalar, (int, float)):
            raise TypeError("Умножение Vector2D возможно только на int|float!")
        return Vector2D(self._x * scalar, self._y * scalar)
    def __rmul__(self, scalar: float|int) -> "Vector2D":
        return self.__mul__(scalar)

    def __abs__(self) -> float|int:
        return math.sqrt(self._x**2 + self._y**2)

    def __matmul__(self, other: "Vector2D") -> float|int:
        if not isinstance(other, Vector2D):
            raise TypeError(f"Математическое умножение Vector2D возможно только с другим Vector2D!")

        return self._x * other.x + self._y * other.y

    def dot(self, other: "Vector2D") -> float|int:
        return self.__matmul__(other)

if __name__ == "__main__":
    vector_1 = Vector2D.from_points((1, 1), (4, 5))
    vector_2 = Vector2D.from_points((-1, 2), (3, 0))

    displacement = Vector2D(-4, 6)

    print(vector_1 + displacement)



