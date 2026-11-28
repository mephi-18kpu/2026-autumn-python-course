from abc import ABC, abstractmethod, abstractclassmethod


class Trajectory(ABC):

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass

class TrajectoryFactory(ABC):

    @abstractclassmethod
    def from_console(cls) -> Trajectory:
        pass
