import sched
import time
import matplotlib.pyplot as plt
import numpy as np

s = sched.scheduler(time.time, time.sleep)
mult = 1.0

# Generates a list of points representing the semicircular curve between a and b
# (The curve always faces "outward")
def generate_curve(point_a, point_b):
    point_list = []
    x_dist = point_b[0] - point_a[0]
    y_dist = point_b[1] - point_a[1]
    dist = (x_dist ** 2 + y_dist ** 2) ** .5
    num_points = 10 * int(np.pi * dist / 2)
    theta = np.arctan(y_dist / x_dist)
    t = np.linspace(theta, theta + np.pi, num_points)
    sign = -1 if x_dist > 0 else 1

    for i in range(num_points):
        x = (point_a[0] + point_b[0]) / 2 + sign * (dist / 2) * np.cos(t[i])
        y = (point_a[1] + point_b[1]) / 2 + sign * (dist / 2) * np.sin(t[i])
        point_list.append([x, y])

    return point_list


# Generates a list of points representing the line segment between a and b
def generate_segment(point_a, point_b):
    point_list = []
    x_dist = point_b[0] - point_a[0]
    y_dist = point_b[1] - point_a[1]
    dist = (x_dist ** 2 + y_dist ** 2) ** .5
    num_dots = int(
        10 * dist)  # creates a ratio between the distance and number of steps

    for i in range(num_dots):
        x = point_a[0] + x_dist / num_dots * i
        y = point_a[1] + y_dist / num_dots * i
        point_list.append([x, y])
    return point_list


# Generates a list of time points representing the quadrilateral
# defined by a, b, c, and d
def generate_quadrilateral(point_a, point_b, point_c, point_d):
    a = generate_segment(point_a, point_b)
    b = generate_segment(point_b, point_c)
    c = generate_segment(point_c, point_d)
    d = generate_segment(point_d, point_a)
    return a + b + c + d

def generate_loop(point_a, point_b, point_c, point_d):
    a = generate_curve(point_a, point_b)
    b = generate_segment(point_b, point_c)
    c = generate_curve(point_c, point_d)
    d = generate_segment(point_d, point_a)
    return a + b + c + d

def plot_shape(point_list):
    for point in point_list:
        plt.plot(point[0], point[1], 'bo')
        plt.draw()
        plt.pause(.01 / mult)


# Draws a loop given 4 points in a rectangular pattern
def plot_loop(point_a, point_b, point_c, point_d):
    a = generate_curve(point_a, point_b)
    b = generate_segment(point_b, point_c)
    c = generate_curve(point_c, point_d)
    d = generate_segment(point_d, point_a)

    s.enter(0 / mult, 2, plot_shape, [a])
    s.enter(2 / mult, 2, plot_shape, [b])
    s.enter(4 / mult, 2, plot_shape, [c])
    s.enter(6 / mult, 2, plot_shape, [d])
    s.run()


def main():
    # Set the plot boundaries
    plt.figure("Loop", figsize=(8, 8))
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)

    # Some example loops
    # draw_loop([1, 1], [-1, 1], [-1, -1], [1, -1])
    draw_loop([1, 0], [0, 1], [-1, 0], [0, -1])
    # plot_shape(generate_quadrilateral([1, 0], [0, 1], [-1, 0], [0, -1]))

    plt.show()


if __name__ == '__main__':
    main()
