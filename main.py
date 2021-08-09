"""
SpaceTraveler.

@author         Andrés Uribe Stengel
@lastModified   09.08.2021
"""

# Imports
from src.space import Space
from src.ufo import UFO
from src.utils import read_json_config
from src.utils import plot_trajectory


if __name__ == '__main__':
    # Read and set the user-defined parameters
    max_coordinate, n_planets = read_json_config()

    # Initialize the space object with the parameters
    space = Space(max_coordinate=max_coordinate, n_planets=n_planets)

    # Initialize the ufo object within space
    ufo = UFO(space=space)

    # Start the ufo's trajectory
    ufo.move()

    # Plot its trajectory when the ufo either successfully escapes or crashes
    plot_trajectory(space=space, ufo=ufo)
