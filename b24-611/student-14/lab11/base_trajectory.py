import operator
from abc import ABC, abstractmethod,abstractclassmethod
from math import cos, hypot, pi, sin
from types import NotImplementedType

class Trajectory(ABC):

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass

class TrajectoryFactory(ABC):

    @abstractmethod
    def from_console(cls):
        pass

