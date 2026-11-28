import math
from abc import ABC, abstractmethod, abstractproperty, abstractclassmethod


class Vector2D:
    DIMENSION = 2

    def __init__(self, x: float, y: float) -> None:
        self._x = x
        self._y = y

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    def __repr__(self) -> str:
        return f"Вектор2D({self._x}, {self._y})"

    def __add__(self, other: "Vector2D") -> "Vector2D":
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self._x + other._x, self._y + other._y)

    def __mul__(self, scalar: float) -> "Vector2D":
        return Vector2D(self._x * scalar, self._y * scalar)

    def __rmul__(self, scalar: float) -> "Vector2D":
        return self.__mul__(scalar)

    def __abs__(self) -> float:
        return math.hypot(self._x, self._y)

    def __matmul__(self, other: "Vector2D") -> float:
        return self.dot(other)

    def dot(self, other: "Vector2D") -> float:
        return self._x * other._x + self._y * other._y

    @staticmethod
    def _normalize_index(index: int) -> int:
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть целым числом")
        if index == 0 or index == -2:
            return 0
        elif index == 1 or index == -1:
            return 1
        else:
            raise IndexError("Индекс выходит за границы вектора")

    def __getitem__(self, index: int) -> float:
        norm_idx = self._normalize_index(index)
        return self._x if norm_idx == 0 else self._y

    def __setitem__(self, index: int, value: float) -> None:
        norm_idx = self._normalize_index(index)
        if norm_idx == 0:
            self._x = value
        else:
            self._y = value

    @classmethod
    def from_points(cls, start: tuple, end: tuple) -> "Vector2D":
        return cls(end[0] - start[0], end[1] - start[1])


class Trajectory(ABC):
    @abstractmethod
    def __call__(self, t: float) -> Vector2D:
        pass


class TrajectoryFactory(ABC):
    @abstractclassmethod
    def from_console(cls):
        pass


#############
class ParabolicTrajectory(Trajectory):
    def __init__(self, a: float, b: float, c: float) -> None:
        if a == 0:
            raise ValueError("Коэффициент 'a' не может быть равен 0 (это будет прямая, а не парабола)")
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, t: float) -> Vector2D:
        x = t
        y = self.a * (t**2) + self.b *t + self.c
        return Vector2D(x, y)


############
class HyperbolicTrajectory(Trajectory):
    def __init__(self, a: float, b: float, branch: int = 1) -> None:
        if a <= 0 or b <= 0:
            raise ValueError("Параметры 'a' и 'b' должны быть больше нуля")
        if branch not in (1, -1):
            raise ValueError("Параметр 'branch' должен быть 1 или -1")
        self.a = a
        self.b = b
        self.branch = branch

    def __call__(self, t: float) -> Vector2D:
        x = self.branch * self.a * math.cosh(t)
        y = self.b * math.sinh(t)
        return Vector2D(x, y)

