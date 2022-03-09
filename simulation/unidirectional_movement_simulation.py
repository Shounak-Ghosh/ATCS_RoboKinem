import matplotlib.pyplot as plt
import math
import numpy as np
import circle as c
import shapes as sh
import spline as sp
import time


def plot_vectors(point_list):
    for i in range(len(point_list) - 1):
        x_dist = point_list[i + 1][0] - point_list[i][0]
        y_dist = point_list[i + 1][1] - point_list[i][1]
        # vector_list.append([x_dist,y_dist])
        # plt.plot(x_dist,y_dist,'bo')
        vector_length = math.sqrt(x_dist ** 2 + y_dist ** 2)
        if vector_length != 0:
            scale = 50 / vector_length
        else:
            scale = 1
        x_dist *= scale
        y_dist *= scale
        print(x_dist, y_dist, y_dist - x_dist, y_dist + x_dist)
        plt.plot(i, x_dist, 'ro')  # should be sin (for circle)
        plt.plot(i, y_dist, 'g^')  # should be -cos (for circle)
        plt.draw()


def main():
    # c_scale = 2000  # simply using 1 leads to very small vector values
    # plt.figure("Circle Vector Simulation", figsize=(8, 8))
    # plt.ylabel("Vector values")
    # plt.xlabel("Time")
    # plot_vectors(c.generate_circle([-c_scale, 0], [c_scale, 0]))


    plt.figure("Loop Vector Simulation", figsize=(8, 8))
    plt.ylabel("Vector values")
    plt.xlabel("Time")
    # plot_vectors(sh.generate_loop([1, 1], [-1, 1], [-1, -1], [1, -1]))
    # Diagonal loop
    # plot_vectors(sh.generate_loop([1, 0], [0, 1], [-1, 0],
    #                                             [0, -1]))
    plot_vectors(sp.generate_spline([[0, 1], [1, 3], [2, 2]]))
    plt.show()


if __name__ == '__main__':
    main()
