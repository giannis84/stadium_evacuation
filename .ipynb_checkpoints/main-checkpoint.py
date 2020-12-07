# SIMULATIONS OF COMPLEX SYSTEMS
# 2020 Project: Simulation of stadium evacuation
# Collaborators: Alfred Bergsten, Giannis Kostaras, Mohammad Zoubi, Andreas Spetz

import numpy as np
import matplotlib.pyplot as plt
import stadium
import templates


def print_info(name):
    print(f'Project: {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def visualize(grid):
    plt.imshow(grid, interpolation='nearest')
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_info('Stadium evacuation simulation.')
    stadium = stadium.create_stadium(templates.test_template)
    visualize(stadium)
