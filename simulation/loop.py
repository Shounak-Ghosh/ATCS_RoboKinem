import sched
import time
import matplotlib.pyplot as plt
import numpy as np

s = sched.scheduler(time.time, time.sleep)
mult = 1.0

# Set the plot boundaries
plt.figure("Loop", figsize=(8, 8))
plt.xlim(-4, 4)
plt.ylim(-4, 4)


# Draws a semicircular curve between two points
def draw_curve(point_a, point_b):
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
        plt.plot(x, y, 'bo')
    
        plt.draw()
        plt.pause(.01 / mult)


# Draws a disconnected line segment between two points
def draw_segment(point_a, point_b):
    x_dist = point_b[0] - point_a[0]
    y_dist = point_b[1] - point_a[1]
    dist = (x_dist ** 2 + y_dist ** 2) ** .5
    num_dots = int(
        10 * dist)  # creates a ratio between the distance and number of steps

    for i in range(num_dots):
        plt.plot(point_a[0] + x_dist / num_dots * i,
                 point_a[1] + y_dist / num_dots * i, "bo")
        plt.draw()
        plt.pause(.01 / mult)


# Draws a quadrilateral given 4 points in order
def draw_quadrilateral(point_a, point_b, point_c, point_d):
    draw_segment(point_a, point_b)
    draw_segment(point_b, point_c)
    draw_segment(point_c, point_d)
    draw_segment(point_d, point_a)


# Draws a loop given 4 points in a rectangular pattern
def draw_loop(point_a, point_b, point_c, point_d):
    s.enter(0 / mult, 2, draw_curve, argument=(point_a, point_b))
    s.enter(2 / mult, 2, draw_segment, argument=(point_b, point_c))
    s.enter(4 / mult, 2, draw_curve, argument=(point_c, point_d))
    s.enter(6 / mult, 2, draw_segment, argument=(point_d, point_a))
    s.run()


# Some example loops
# draw_loop([1, 1], [-1, 1], [-1, -1], [1, -1])
draw_loop([1, 0], [0, 1], [-1, 0], [0, -1])
plt.show()
