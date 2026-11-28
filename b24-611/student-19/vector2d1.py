import math

class Vector2D:

    DIMENSION = 2

    def __init__(self, x: float|int, y: float|int):
        self._x = x
        self._y = y

    @classmethod
    def from_points(cls,
                    start: tuple[float | int, float | int],
                    end: tuple[float | int, float | int]) -> "Vector2D":

        start_x, start_y = start
        end_x, end_y = end
        return cls(end_x - start_x, end_y - start_y)

    @property
    def x(self) -> float|int:
        return self._x

    @property
    def y(self) -> float | int:
        return self._y

    def __str__(self) -> str:
        return f"Vector({self.x, self.y})"

    def __repr__(self) -> str:
        return f"Vector (id == {id(self)}) with .x = {self.x}, .y = {self.y}"

    def __add__(self, other: "Vector2D") -> "Vector2D":
        if not isinstance(other, Vector2D):
            raise TypeError("slogenie suppots with other Vector2D ")
        return Vector2D(self._x + other._x, self.y+other._y)

    def __mul__(self, scalar: float|int) -> "Vector2D":
        if not isinstance(scalar, (int, float)):
            raise TypeError("slogenie suppots with scalar")
        return Vector2D(self._x * scalar, self._y * scalar)

    def __rmul__(self, scalar: float|int) -> "Vector2D":
        return self.__mul__(scalar)

    def __abs__(self) -> float|int:
        return math.sqrt(self._x**2 + self._y**2)

    def __matmul__(self, other: "Vector2D") -> float|int:
        if not isinstance(other, Vector2D):
            raise TypeError(f"Math multik Vector2D s mission impossible")
        return self._x * other._x + self._y * other._y

    def dot(self, other: "Vector2D") -> float|int:
        return self.__matmul__(other)

    def __getitem__(self, key) -> float|int:
        if isinstance(key, str):
            if key == "x":
                return self._x
            elif key == "y":
                return self._y
            raise KeyError(f"atmpt to get ureal engine 5 x/y with key {key} ")
        if isinstance(key, int):
            index = self._normalize_index(key, Vector2D.DIMENSION)
            if index == 0:
                return self._x
            if index == 1:
                return self._y
        raise TypeError(f"unsupported type (key = {type(key)}")

    def __setitem__(self, key, value):
        if isinstance(key, str):
            if key == "x":
                self._x = value
                return
            elif key == "y":
                self._y = value
                return
            raise KeyError(f"atmpt to get ureal engine 5 x/y with key {key} ")
        if isinstance(key, int):
            index = self._normalize_index(key, Vector2D.DIMENSION)
            if index == 0:
                self._x = value
                return
            if index == 1:
                self._y = value
                return
        raise TypeError(f"unsupported type (key = {type(key)}")

    @staticmethod
    def _normalize_index(index: int, size: int):
        if index < 0:
            index += size
        if index < 0 or index >= size:
            raise IndexError("indexes out of diapozone")
        return index

if __name__ == "__main__":
    vector_1 = Vector2D(1, 5)
    vector_2 = Vector2D.from_points((-1, 2), (3, 5))

    displacement = Vector2D(-1, -2)
    displacement["x"] = 3

    print(vector_1 + displacement)
    print(vector_1 @ vector_2)
    print(vector_1 + 2 * displacement)

