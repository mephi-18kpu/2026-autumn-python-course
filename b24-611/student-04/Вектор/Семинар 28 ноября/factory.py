import operator
from abc import ABC, abstractmethod, abstractclassmethod
from math import cos, hypot, pi, sin
from types import NotImplementedType

class Trajectory(ABC):
    """Параметрическая кривая на плоскости."""

    @abstractmethod
    def __call__(self, *args, **kwargs) -> Vector2D:
        pass
        """Вернуть положение на кривой для параметра t."""
        ...
class Tragectoryfactory(ABC):

    @abstractclassmethod
    def from_console(cls) -> Trajectory:
        pass
