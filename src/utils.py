"""
Utils.

@author         Andrés Uribe Stengel
@lastModified   09.08.2021
"""


# Imports
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
    print('\n## Configuration parameters are being read from JSON')

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

    # Informational prints
    print('Space border in x- and y-axis direction: ', max_coordinate)
    print('Number of planets in space: ', n_planets, '\n')

    return max_coordinate, n_planets


def plot_trajectory(space, ufo):
    """
    Plots the ufo's trajectory on an n x n grid.

    :param space: (Space) The generated space object.
    :param ufo: (UFO) The generated ufo object.
    """
    print('## UFO trajectory is being plotted\n')

    # Informational print
    print('## Close the trajectory plot to play again.\n')

    # Create a matplotlib scatter-plot with the planet's coordinates
    fig, ax = plt.subplots()
    ax.scatter(space.planets[:, 0], space.planets[:, 1], c='royalblue')

    # Plot the ufo's trajectory line
    line = lines.Line2D(ufo.history[:, 0], ufo.history[:, 1], color='firebrick')
    ax.add_line(line)

    # Set plot title
    ax.set_title('SpaceTraveler')

    # Set the x- and y-axis labels and limits according to the maximum defined coordinate
    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')
    plt.xlim((0, space.max_coordinate + 1))
    plt.ylim((0, space.max_coordinate + 1))

    # Show all x- and y-axis ticks and reduce font size them to avoid overlap
    ax.set_xticks(np.arange(space.max_coordinate + 1))
    ax.set_yticks(np.arange(space.max_coordinate + 1))
    plt.setp(ax.get_xticklabels(), fontsize='x-small')
    plt.setp(ax.get_yticklabels(), fontsize='x-small')

    # Add a custom legend
    legend_elements = \
        [lines.Line2D([0], [0], marker='o', color='w', label='Planets', markerfacecolor='royalblue', markersize=10),
         lines.Line2D([0], [0], color='firebrick', lw=2, label='UFO Trajectory')]
    ax.legend(handles=legend_elements, loc='best')

    # Add a grid
    plt.grid()

    # Set the plot's x- and y-axis proportion to be equal
    plt.gca().set_aspect('equal', adjustable='box')

    # Show the plot
    plt.show()
