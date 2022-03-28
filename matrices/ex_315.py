import numpy as np
import math
import ex_32 as rot


def transformation_mat(rot_mat, p):
    """
    Returns the transformation matrix for the rotation matrix and point p
    @param rot_mat: rotation matrix
    @param p: point in homogeneous coordinates
    @return: transformation matrix
    """
    t = np.array([[1, 0, 0, p[0]], [0, 1, 0, p[1]],
                 [0, 0, 1, p[2]], [0, 0, 0, 1]])
    return np.matmul(rot_mat, t)


def main():
    """
    Main function
    """
    t_ab = np.array(
        [[1 / 2 ** .5, -1 / 2 ** .5, 0, -1], [1 / 2 ** .5, 1 / 2 ** .5, 0, 0],
         [0, 0, 1, 1], [0, 0, 0, 1]])

    t_cb = np.array([[1 / 2 ** .5, 0, 1 / 2 ** .5, 0], [0, 1, 0, 1],
                     [-1 / 2 ** .5, 0, 1 / 2 ** .5, 0], [0, 0, 0, 1]])
    t_ba = np.linalg.inv(t_ab)
    t_ca = np.matmul(t_cb, t_ba)
    print("\npart (c)")
    print(t_ca)


if __name__ == '__main__':
    main()
