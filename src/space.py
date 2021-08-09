"""
Space.

@author         Andrés Uribe Stengel
@lastModified   08.08.2021
"""


import numpy as np
from src.planet import Planet


class Space:
    def __init__(self, max_coordinate, n_planets):
        self.x_start_coordinate = 0
        self.y_start_coordinate = 0

        self.max_coordinate = max_coordinate

        self.n_planets = n_planets
        self.planets = self.set_planets()

    def set_planets(self):
        planets = np.empty((self.n_planets, 2))

        for cnt in range(0, self.n_planets):
            planet_coordinates = np.random.randint(low=1, high=self.max_coordinate, size=2)

            planet = Planet(planet_coordinates)

            planets[cnt] = planet.coordinates

        return planets
