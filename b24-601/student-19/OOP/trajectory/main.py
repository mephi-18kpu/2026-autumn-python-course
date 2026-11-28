from cmath import cos

from fontTools.misc.vector import Vector

from OOP.trajectories import Vector2D
from lineTrajectory import LinearTrajectory, LinearTrajectoryFactory
from baseTrajectory import  Trajectory, TrajectoryFactory
import math


class EclipticTrajectory(Trajectory):
    def __init__(self, a: float|int, b: float|int):
        if not (a>0 and b>0):
            raise ValueError("a and b must be positive")
        self._a = a
        self._b = b

    def __call__(self, t: float|int):
        return Vector2D(self._a*math.cos(t),self._b*math.sin(t))


trajectory = LinearTrajectoryFactory.from_console()
print(trajectory(5))
