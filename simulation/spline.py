import scipy
from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt


def generate_spline(def_point_list):
    min_x = def_point_list[0][0]
    max_x = def_point_list[0][1]
    x_vals = []
    y_vals = []
    for point in def_point_list:
        x_vals.append(point[0])
        min_x = min(min_x, point[0])
        max_x = max(max_x, point[0])
        y_vals.append(point[1])
    f = CubicSpline(x_vals, y_vals, bc_type='natural')
    point_list = []
    for x in np.linspace(min_x, max_x, 100):
        point_list.append([x, f(x)])
    return point_list


def plot_shape(point_list):
    for point in point_list:
        plt.plot(point[0], point[1], 'bo')
        plt.draw()
        plt.pause(.01)


def main():
    plt.style.use('seaborn-poster')

    x = [0, 1, 2, 3]
    y = [0, 3, 2, 4]
    min_x = x[0]
    max_x = x[0]
    point_list = []
    for i in range(len(x)):
        min_x = min(min_x, x[i])
        max_x = max(max_x, x[i])
        point_list.append([x[i], y[i]])

    # use bc_type = 'natural' adds the constraints as we described above
    f = CubicSpline(x, y, bc_type='natural')
    x_new = np.linspace(min_x, max_x, 100)
    y_new = f(x_new)

    plt.figure("Smooth Cubic Spline Interpolation", figsize=(8, 8))
    plt.plot(x_new, y_new, 'b')
    plt.plot(x, y, 'ro')
    plt.title('Smooth Cubic Spline Interpolation')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.figure("Point Cubic Spline Interpolation", figsize=(8, 8))
    plot_shape(generate_spline(point_list))
    plt.plot(x, y, 'rD')
    plt.draw()
    plt.title('Point Cubic Spline Interpolation')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()


if __name__ == '__main__':
    main()
