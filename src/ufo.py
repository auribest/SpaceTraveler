"""
UFO.

@author         Andrés Uribe Stengel
@lastModified   09.08.2021
"""


# Imports
import numpy as np
from random import randint


class UFO:
    """
    The ufo class.
    """
    def __init__(self, space):
        # Set the initialized space
        self.space = space

        # Set the ufo's coordinates according the the space starting point
        self.coordinates = np.array([space.x_start_coordinate, space.y_start_coordinate])

        # Initialize the ufo's history with the starting coordinates
        self.history = np.array([self.coordinates])

    def move(self):
        """
        Defines the ufo's trajectory and how it is influenced by the nearest planet.
        """
        while True:
            # Initialize the unaltered ufo step per iteration (+1 in x- and y-axis direction)
            travel_course = np.array([1, 1])

            # Set the new ufo coordinates with the unaltered travel course
            self.coordinates = np.add(self.coordinates, travel_course)

            # Check if the ufo has crashed with a planet or escaped successfully
            end = self.check_end_journey()
            if end:
                break

            # Get the distance of the closest planet
            min_distance_vector = self.calculate_closest_planet()

            # Get the index of the direction that will be altered in the travel course
            # If the x-axis distance is larger, set the altered direction index to 0 (x-axis direction)
            # If the y-axis distance is larger, set the altered direction index to 1 (y-axis direction)
            # If the x- and y-axis distances are equal, set the altered direction randomly
            direction_index = None
            if abs(min_distance_vector[0]) > abs(min_distance_vector[1]):
                direction_index = 0
            elif abs(min_distance_vector[0]) < abs(min_distance_vector[1]):
                direction_index = 1
            elif abs(min_distance_vector[0]) == abs(min_distance_vector[1]):
                direction_index = randint(0, 1)

            # Initialize the unaltered course
            altered_course = [0, 0]

            # Set the direction (x- or y-axis) in which the course will be altered
            altered_course[direction_index] += 1

            # Alter the course
            self.coordinates = np.add(self.coordinates, altered_course)

            # Check if the ufo has crashed with a planet or escaped successfully
            end = self.check_end_journey()
            if end:
                break

            # Add the new coordinates to the ufo's history
            self.history = np.concatenate((self.history, np.array([self.coordinates])), axis=0)

    def calculate_closest_planet(self):
        """
        Calculates the current closest planet to the ufo.

        :return: (numpy array) The distance vector from the ufo to the planet.
        """
        distance_vectors = np.empty((self.space.n_planets, 2))
        for cnt in range(0, self.space.n_planets):
            distance_vectors[cnt] = np.subtract(self.space.planets[cnt], self.coordinates)

        distances = np.empty((self.space.n_planets, 1))
        for cnt in range(0, len(distance_vectors)):
            distances[cnt] = int((abs(distance_vectors[cnt][0]) + abs(distance_vectors[cnt][1])) / 2)

        min_distance_index = np.argmin(distances)
        min_distance_vector = distance_vectors[min_distance_index]

        return min_distance_vector

    def check_end_journey(self):
        """
        Checks if the ufo either crashed or escaped successfully and if so, returns a positive termination feedback.

        :return: (bool) True or False.
        """
        # Compare all planet coordinates with the ufo coordinates and if one matches, the ufo has crashed
        for planet in self.space.planets:
            if self.coordinates[0] == planet[0] and self.coordinates[1] == planet[1]:
                self.history = np.concatenate((self.history, np.array([self.coordinates])), axis=0)
                print('Your ship has crashed!!!')

                return True

        # If the coordinates are outside of space, the ufo escaped successfully
        if self.coordinates[0] > self.space.max_coordinate and self.coordinates[1] > self.space.max_coordinate:
            self.history = np.concatenate((self.history, np.array([self.coordinates])), axis=0)
            print('You have evaded all planets successfully!!!')

            return True
