from mpl_toolkits import mplot3d
import math
import numpy as np
import matplotlib.pyplot as plt

W = 0
THETA = 0

# returns the skew symmetric representation of the vector w
def skew_symmetric(w):
    return np.array([[0, -w[2], w[1]], [w[2], 0, -w[0]], [-w[1], w[0], 0]])


# w is the unit vector around which our coordinate axes are being rotated
# theta is the scalar amount telling us how "much" to rotate
def mat_exp(w, theta):
    # w_ss = skew_symmetric(w)
    return np.identity(3) + np.sin(theta) * w + (
            1 - np.cos(theta)) * np.matmul(w, w)


def mat_log(rot_mat):
    global W
    global THETA
    # need to find matrix log of the given SO(3) matrix: Thus the matrix logarithm algorithm
    # IF R = I then theta = 0 and w^ is undefined
    if np.array_equal(rot_mat, np.identity(3)):
        return 0
    # IF tr(R) = -1, then theta = pi and w is 1 of 3 given forms
    elif np.trace(rot_mat) == 1:
        theta = np.pi
        w = 1.0 / sqrt(2.0 * (1 + rot_mat[0][0])) * np.array(
            [1 + rot_mat[0][0], rot_mat[1][0], rot_mat[2][0]])
        W = w
        THETA = theta
        return w * theta
    else:  # ELSE theta = cos^-1(1/2(tr(R)-1)), w of a given form
        theta = np.arccos(.5 * (np.trace(rot_mat) - 1))
        w = 1.0 / (2.0 * np.sin(theta)) * (rot_mat - rot_mat.T)
        W = w
        THETA = theta
        return w * theta


def main():
    rot_mat = np.array([[0, -1, 0], [0, 0, -1], [1, 0, 0]])
    out_mat = mat_log(rot_mat)
    print("skew symmetric W")
    print(W)
    print("theta:", THETA,"\n")
    print("(w * theta) matrix")
    print(out_mat)
    print("\nInitial matrix")
    print(mat_exp(W, THETA))


if __name__ == '__main__':
    main()
