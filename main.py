"""
SpaceTraveler.

@author         Andrés Uribe Stengel
@lastModified   08.08.2021
"""


from src.space import Space
from src.ufo import UFO
from src.utils import plot_trajectory


if __name__ == '__main__':
    max_coordinate = 20
    n_planets = 15

    space = Space(max_coordinate=max_coordinate, n_planets=n_planets)

    ufo = UFO(space=space)

    ufo.move()

    plot_trajectory(space=space, ufo=ufo)
