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
        self.planets = self.create_planets()

        # Informational print
        print('## Space has been created\n')

    def create_planets(self):
        """
        Generate the specified amount of planets in space.

        :return: (numpy array) All planet coordinates.
        """
        print('## Planets are being generated')

        # Create an uninitialized numpy array with it's pre-defined dimensions
        planets = np.empty((self.n_planets, 2))

        # For the amount of specified planets, generate a planet with random coordinates (in the bounds of space)
        for cnt in range(0, self.n_planets):
            # Generate the coordinates
            planet_coordinates = self.set_planet_coordinates(planets=planets)

            # Create the planet
            planet = Planet(planet_coordinates)

            # Add it to the array of planets
            planets[cnt] = planet.coordinates

        # Informational print
        print('All planet coordinates:\n', planets, '\n')

        return planets

    def set_planet_coordinates(self, planets):
        """
        Generate and check if planet coordinates already exist, if they do, re-generate the coordinates.

        :param planets: (numpy array) The current list of generated planets.
        :return: (numpy array) The new planet's coordinates.
        """
        # Generate random coordinates
        planet_coordinates = np.random.randint(low=1, high=self.max_coordinate, size=2)

        # If the coordinates are already in the array of planets, re-generate the random coordinates
        if any(np.equal(planets, planet_coordinates).all(1)):
            self.set_planet_coordinates(planets=planets)

        return planet_coordinates
