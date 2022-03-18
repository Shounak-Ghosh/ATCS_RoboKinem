from mpl_toolkits import mplot3d
import math
import numpy as np
import matplotlib.pyplot as plt


def rot_x(theta):
    rot = np.array([[1, 0, 0], [0, np.cos(theta), -np.sin(theta)],
                    [0, np.sin(theta), np.cos(theta)]])
    return rot


def rot_y(theta):
    rot = np.array([[np.cos(theta), 0, np.sin(theta)], [0, 1, 0],
                    [-np.sin(theta), 0, np.cos(theta)]])
    return rot


def rot_z(theta):
    rot = np.array([[np.cos(theta), -np.sin(theta), 0],
                    [np.sin(theta), np.cos(theta), 0],
                    [0, 0, 1]])
    return rot


def main():
    fig = plt.figure(figsize=(6, 6), label="Exercise 3.2")
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title("Exercise 3.2")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    pt = np.array([1 / math.sqrt(3), -1 / math.sqrt(6), 1 / math.sqrt(2)])
    print("pt", pt)
    ax.scatter(pt[0], pt[1], pt[2], s=100, c='blue', label='original point')

    trans_x = np.matmul(rot_x(np.radians(30)), pt)
    ax.scatter(trans_x[0], trans_x[1], trans_x[2], s=50, c='#b82735',
               label='point after x transformation')  # red

    trans_y = np.matmul(rot_y(np.radians(135)), trans_x)
    ax.scatter(trans_y[0], trans_y[1], trans_y[2], s=50, c='#de4909',
               label='point after y transformation')  # orange

    trans_z = np.matmul(rot_z(np.radians(-120)), trans_y)
    ax.scatter(trans_z[0], trans_z[1], trans_z[2], s=100, c='#09e6de',
               label='point after z transformation')  # cyan
    print("p' coordinates", trans_z)
    r = np.matmul(rot_z(np.radians(-120)),
                  np.matmul(rot_y(np.radians(135)), rot_x(np.radians(30))))
    print("rotation matrix\n", r)
    print("Rp", np.matmul(r, pt))

    # Visual proof that ZYXp does not equal XYZp
    # not_r = np.matmul(rot_x(np.radians(30)),
    #                   np.matmul(rot_y(np.radians(135)),
    #                             rot_z(np.radians(-120))))
    # not_rp = np.matmul(not_r, pt)
    # print("not_Rp", not_rp)
    # ax.scatter(not_rp[0], not_rp[1], not_rp[2], s=100, c='#0fd47b',
    #            label='incorrect transformation')  # green

    plt.legend(loc="upper left")
    plt.show()


if __name__ == '__main__':
    main()
