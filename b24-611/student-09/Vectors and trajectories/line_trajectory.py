#System imports

#External imports
from abc import ABC, abstractmethod, abstractclassmethod

#User imports
from based_trajectory import Trajectory, TrajectoryFactory
from vector_2d import Vector2d

########################

class LinearTrajectory(Trajectory):

    def __init__ (self, start_pos: Vector2d, direction: Vector2d):
        if not isinstance(start_pos, Vector2d) or not isinstance(direction, Vector2d):
            raise TypeError('Where is my Vector2d man?')

        self._start_pos = start_pos
        self._direction = direction

    def __call__(self, t: float):
        return (self._start_pos + t * self._direction)

class LinearTrajectoryFactory(TrajectoryFactory):

    @classmethod
    def from_console(cls)-> Trajectory:
        start_pos_x=float(input('Trj start, x coord '))
        start_pos_y=float(input('Trj start, y coord '))
        direct_pos_x=float(input('Trj direction vector, x coord '))
        direct_pos_y=float(input('Trj direction vector, y coord '))
        return LinearTrajectory(
            Vector2d.from_points((0, 0), (start_pos_x, start_pos_y)),
            Vector2d(direct_pos_x, direct_pos_y)
        )
