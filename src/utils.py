"""
Utils.

@author         Andrés Uribe Stengel
@lastModified   08.08.2021
"""


import os
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines


def read_json_config():
    """
    Loads and returns a set of configuration parameters from a JSON file.

    :return: (tuple) Maximum possible coordinate in space (int) and the number of planets in space (int).
    """
    print('## Configuration parameters are being read from JSON')

    # Set the configuration path
    config_dir = 'config/'

    # Check if config file exists
    if not os.path.isfile(config_dir + 'config.json'):
        raise FileNotFoundError('No JSON config file found!')

    # Open JSON file, load config parameters and close file
    file = open(os.path.join(config_dir + 'config.json'), 'r')
    config = json.load(file)
    file.close()

    # Get the maximum coordinate and the amount of planets
    max_coordinate = config.get('max_coordinate')
    n_planets = config.get('n_planets')

    return max_coordinate, n_planets


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
