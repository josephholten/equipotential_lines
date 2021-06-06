from copy import copy
from math import sqrt

import matplotlib.pyplot as plt
import numpy as np


def plot_equipotential_lines(m_1, m_2, d):
    """
    Plots the equi-gravi-potential lines in the two body system, with masses m_1 and m_2 and the distance between them d

    :param m_1: mass of large object 1
    :param m_2: mass of large object 2
    :param d: distance between the large objects
    :return:
    """

    # "_1" should always indicate a different of same kind (like mass of object one, or object 2)

    q = m_1 / (m_1 + m_2)

    # position of the large objects on the x-axis
    x_1 = (q - 1) * d
    x_2 = q * d

    # distance of the small (test mass) to each of the large masses respectively
    def distance(x, y):
        return sqrt((x - x_1) ** 2 + y ** 2), sqrt((x - x_2) ** 2 + y ** 2)

    # Gravitational constant
    # G = 6.67408E-11
    G = 1

    def eff_potential(x, y):
        d_1, d_2 = distance(x, y)
        return G * (-m_1 / d_1 - m_2 / d_2 - (m_1 + m_2) / (2 * d ** 3) * (x ** 2 + y ** 2))

    # get a vector of x and y values respectively at which to compute the potential
    x_space = np.linspace(-1.3 * d, 1.3 * d, 100)
    y_space = copy(x_space)

    # make a matrix from them
    x_mat, y_mat = np.meshgrid(x_space, y_space)
    # calculate teh potential on the matrix
    z_mat = np.vectorize(eff_potential)(x_mat, y_mat)
    z_mat = -z_mat

    # contour line spacing
    # line_spacing = np.linspace(0, 100, num=35)       # 2
    linear_lines = np.linspace(0, 80, num=35)       # 2
    log_lines = np.logspace(np.log10(81), 3, num=20)  # v3
    # print(linear_lines)
    # print(log_lines)
    # linear_lines = np.append(linear_lines, )
    # print(linear_lines)
    line_spacing = np.append(linear_lines, log_lines)
    #print(line_spacing)

    # plot the contour
    plt.contour(x_space, y_space, z_mat, line_spacing, colors='black')
    plt.axis('off')
    plt.show()


plot_equipotential_lines(1, 40, 1)


