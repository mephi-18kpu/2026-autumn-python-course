#System imports

#External imports
from abc import ABC, abstractmethod, abstractclassmethod

#User imports

########################

class Trajectory(ABC):

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass

class TrajectoryFactory(ABC):

    @abstractclassmethod
    def from_console(cls):
        pass


