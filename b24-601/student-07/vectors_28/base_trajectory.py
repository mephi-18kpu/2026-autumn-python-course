from abc import ABC, abstractmethod

class Trajectory(ABC):

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass

class TranjectoryFactory(ABC):

    @abstractmethod
    def from_console(self) -> Trajectory:
        pass
