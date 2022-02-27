import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import time

script_dir = os.path.dirname( __file__ )
simulation_dir = os.path.join( script_dir, '..','simulation' )
sys.path.append( simulation_dir )
import circle as c


def method1():
    n = 360
    for i in range(n):
        x = np.cos(i * np.pi / 180)  # converting degrees to radians
        y = np.sin(i * np.pi / 180)
        # plt.plot(x, y,'bo')
        plt.plot(i, x, 'ro')
        plt.plot(i, y, 'go')
        time.sleep(.01)
        plt.draw()
    plt.show()

def method2():
    point_list = c.generate_circle([-1, 0], [1, 0])
    # vector_list = []
    for i in range(len(point_list) - 1):
        x_dist = point_list[i + 1][0] - point_list[i][0]
        y_dist = point_list[i + 1][1] - point_list[i][1]
        # vector_list.append([x_dist,y_dist])
        # plt.plot(x_dist,y_dist,'bo')
        plt.plot(i, x_dist, 'ro')
        plt.plot(i, y_dist, 'go')
        plt.draw()
    plt.show()


def main():
    plt.figure("Circle Vector Simulation", figsize=(8, 8))
    # plt.xlim(-2, 2)
    # plt.ylim(-2, 2)
    method2()


if __name__ == '__main__':
    main()
