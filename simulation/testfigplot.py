import matplotlib.pyplot as plt

# plotting a yellow background
# graph with dpi => 50
plt.figure(num='label',
		facecolor='yellow',
		figsize=[10, 7],
		dpi=50)

def draw_segment(point_a, point_b):
    xDist = point_b[0] - point_a[0]
    yDist = point_b[1] - point_a[1]
    dist = (xDist ** 2 + yDist ** 2) ** .5
    numDots = int(
        10 * dist)  # creates a ratio between the distance and number of steps

    for i in range(numDots):
        plt.plot( point_a[0] + xDist / numDots * i,
                 point_a[1] + yDist / numDots * i, "bo")
        plt.draw()
        plt.pause(.01)


def plot_quadrilateral(point_a, point_b, point_c, point_d):
    # minX = min([point_a[0], point_b[0], point_c[0], point_d[0]])
    # maxX = max([point_a[0], point_b[0], point_c[0], point_d[0]])
    # minY = min([point_a[1], point_b[1], point_c[1], point_d[1]])
    # maxY = max([point_a[1], point_b[1], point_c[1], point_d[1]])
    # plt.axis([minX - .1, maxX + .1, minY - .1, maxY + .1])

    draw_segment(point_a, point_b)
    draw_segment(point_b, point_c)
    draw_segment(point_c, point_d)
    draw_segment(point_d, point_a)
    plt.show()


# plot_quadrilateral([0,0],[1,1],[0,2],[-1,1],10)
plot_quadrilateral([1, 1], [2, 2], [2, 1], [1, 0])
