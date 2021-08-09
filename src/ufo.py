"""
UFO.

@author         Andrés Uribe Stengel
@lastModified   08.08.2021
"""


import numpy as np
from random import randint


class UFO:
    def __init__(self, space):
        self.space = space

        self.coordinates = np.array([space.x_start_coordinate, space.y_start_coordinate])

        self.history = np.array([self.coordinates])

    def move(self):
        while True:
            travel_course = np.array([1, 1])

            self.coordinates = np.add(self.coordinates, travel_course)

            end = self.check_end_journey()
            if end:
                break

            min_distance_vector = self.calculate_closest_planet()

            direction_index = None

            if abs(min_distance_vector[0]) > abs(min_distance_vector[1]):
                direction_index = 0
            elif abs(min_distance_vector[0]) < abs(min_distance_vector[1]):
                direction_index = 1
            elif abs(min_distance_vector[0]) == abs(min_distance_vector[1]):
                direction_index = randint(0, 1)

            altered_course = [0, 0]

            altered_course[direction_index] += 1

            self.coordinates = np.add(self.coordinates, altered_course)

            end = self.check_end_journey()
            if end:
                break

            self.history = np.concatenate((self.history, np.array([self.coordinates])), axis=0)

    def calculate_closest_planet(self):
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
        for planet in self.space.planets:
            if self.coordinates[0] == planet[0] and self.coordinates[1] == planet[1]:
                self.history = np.concatenate((self.history, np.array([self.coordinates])), axis=0)
                print('Your ship has crashed!!!')

                return True
            elif self.coordinates[0] > self.space.max_coordinate and self.coordinates[1] > self.space.max_coordinate:
                self.history = np.concatenate((self.history, np.array([self.coordinates])), axis=0)
                print('You have evaded all planets successfully!!!')

                return True
