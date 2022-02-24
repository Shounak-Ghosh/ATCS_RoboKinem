import matplotlib.pyplot as plt

# Set the plot boundaries
plt.figure("Quadrilateral", figsize=(8, 8))
plt.xlim(0, 2.5)
plt.ylim(-.5, 2.5)


# Draws a disconnected line segment between two points
def draw_segment(point_a, point_b):
    xDist = point_b[0] - point_a[0]
    yDist = point_b[1] - point_a[1]
    dist = (xDist ** 2 + yDist ** 2) ** .5
    numDots = int(
        10 * dist)  # creates a ratio between the distance and number of steps

    for i in range(numDots):
        plt.plot(point_a[0] + xDist / numDots * i,
                 point_a[1] + yDist / numDots * i, "bo")
        plt.draw()
        plt.pause(1)


# Draws a quadrilateral given 4 points in order
def draw_quadrilateral(point_a, point_b, point_c, point_d):
    draw_segment(point_a, point_b)
    draw_segment(point_b, point_c)
    draw_segment(point_c, point_d)
    draw_segment(point_d, point_a)


# Some example quadrilaterals
# draw_quadrilateral([0,0],[1,1],[0,2],[-1,1],10)
draw_quadrilateral([1, 1], [2, 2], [2, 1], [1, 0])
plt.show()
