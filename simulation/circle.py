import matplotlib.pyplot as plt
import numpy as np

# Set the plot boundaries
plt.figure("Circle", figsize=(8, 8))
plt.xlim(-2, 2)
plt.ylim(-2, 2)


# Draws a circle given 2 points forming the diameter
def circle(point_a, point_b):
    point_list = []
    xDist = point_b[0] - point_a[0]
    yDist = point_b[1] - point_a[1]
    dist = (xDist ** 2 + yDist ** 2) ** .5
    numpoints = 60
    t = np.linspace(0, 2 * np.pi, numpoints)
    sign = -1 if xDist > 0 else 1

    for i in range(numpoints):
        x = (point_a[0] + point_b[0]) / 2 + sign * (dist / 2) * np.cos(t[i])
        y = (point_a[1] + point_b[1]) / 2 + sign * (dist / 2) * np.sin(t[i])
        point_list.append([x, y])
    return point_list


def plot_circle(point_list):
    for point in point_list:
        plt.plot(point[0], point[1], 'bo')
        plt.draw()
        plt.pause(.01)
    plt.show()


plot_circle(circle([-1, 0], [1, 0]))
plt.show()
