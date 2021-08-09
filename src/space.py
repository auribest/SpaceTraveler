"""
Space.

@author         Andrés Uribe Stengel
@lastModified   09.08.2021
"""


# Imports
import numpy as np
from src.planet import Planet


class Space:
    """
    The space class.
    """
    def __init__(self, max_coordinate, n_planets):
        # Initialize the starting coordinates
        self.x_start_coordinate = 0
        self.y_start_coordinate = 0

        # Set the maximum coordinate in space
        self.max_coordinate = max_coordinate

        # Set and generate the amount of specified planets in space
        self.n_planets = n_planets
        self.planets = self.set_planets()

    def set_planets(self):
        """
        Generate the specified amount of planets in space.

        :return: (numpy array) All planet coordinates.
        """
        # Create an uninitialized numpy array with it's pre-defined dimensions
        planets = np.empty((self.n_planets, 2))

        # For the amount of specified planets, generate a planet with random coordinates (in the bounds of space)
        for cnt in range(0, self.n_planets):
            planet_coordinates = np.random.randint(low=1, high=self.max_coordinate, size=2)

            planet = Planet(planet_coordinates)

            planets[cnt] = planet.coordinates

        return planets
