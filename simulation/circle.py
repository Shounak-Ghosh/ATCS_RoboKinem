import matplotlib.pyplot as plt
import numpy as np


# Draws a circle given 2 points forming the diameter
def generate_circle(point_a, point_b):
    point_list = []
    x_dist = point_b[0] - point_a[0]
    y_dist = point_b[1] - point_a[1]
    dist = (x_dist ** 2 + y_dist ** 2) ** .5
    numpoints = 360
    t = np.linspace(0, 2 * np.pi, numpoints)
    sign = -1 if x_dist > 0 else 1

    for i in range(numpoints):
        x = (point_a[0] + point_b[0]) / 2 + sign * (dist / 2) * np.cos(t[i])
        y = (point_a[1] + point_b[1]) / 2 + sign * (dist / 2) * np.sin(t[i])
        point_list.append([x, y])
    return point_list


def plot_circle(point_list):
    for point in point_list:
        plt.plot(point[0], point[1], 'bo')
        plt.draw()
        plt.pause(1)
    plt.show()


def main():
    # Set the plot boundaries
    plt.figure("Circle", figsize=(8, 8))
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)

    point_list = generate_circle([-1, 0], [1, 0])
    print(point_list)
    plot_circle(point_list)


if __name__ == "__main__":
    main()
