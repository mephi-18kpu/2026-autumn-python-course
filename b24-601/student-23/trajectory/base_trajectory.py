from abc import ABC, abstractclassmethod

class Trajectory(ABC):

    @abstractclassmethod
    def __call__(self, *args, **kwargs):
        pass

class TrajectoryFactory(ABC):

    @abstractclassmethod
    def from_console(cls) -> Trajectory:
        pass
