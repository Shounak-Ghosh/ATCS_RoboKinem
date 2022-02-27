import matplotlib.pyplot as plt
import numpy as np
import circle as c
import loop as l
import time


def plot_vectors(point_list):
    for i in range(len(point_list) - 1):
        x_dist = point_list[i + 1][0] - point_list[i][0]
        y_dist = point_list[i + 1][1] - point_list[i][1]
        # vector_list.append([x_dist,y_dist])
        # plt.plot(x_dist,y_dist,'bo')
        plt.plot(i, x_dist, 'ro')  # should be sin
        plt.plot(i, y_dist, 'go')  # should be -cos
        plt.draw()


def main():
    plt.figure("Circle Vector Simulation", figsize=(8, 8))
    plot_vectors(c.generate_circle([-1, 0], [1, 0]))

    plt.figure("Loop Vector Simulation", figsize=(8, 8))
    plot_vectors(l.generate_loop([1, 1], [-1, 1], [-1, -1], [1, -1]))
    plt.show()


if __name__ == '__main__':
    main()
