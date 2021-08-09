"""
Utils.

@author         Andrés Uribe Stengel
@lastModified   08.08.2021
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines


def plot_trajectory(space, ufo):
    fig, ax = plt.subplots()
    ax.scatter(space.planets[:, 0], space.planets[:, 1])

    plt.xlim((0, space.max_coordinate + 1))
    plt.ylim((0, space.max_coordinate + 1))
    ax.set_xticks(np.arange(space.max_coordinate + 1))
    ax.set_yticks(np.arange(space.max_coordinate + 1))

    plt.grid()

    line = lines.Line2D(ufo.history[:, 0], ufo.history[:, 1], color='red')
    ax.add_line(line)

    plt.gca().set_aspect('equal', adjustable='box')

    plt.show()
