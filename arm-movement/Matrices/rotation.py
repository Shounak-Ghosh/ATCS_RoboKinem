import numpy as np
import math


def x(points, angle):
    a = np.deg2rad(angle)
    matrix = ([1, 0, 0],
              [0, np.cos(a), -1 * np.sin(a)],
              [0, np.sin(a), np.cos(a)])
    return np.matmul(matrix, points)


def y(points, angle):
    a = np.deg2rad(angle)
    matrix = ([cos(a), 0, sin(a)], [0, 1, 0], [-1 * sin(a), 0, cos(a)])
    return np.matmul(matrix, points)


def z(points, angle):
    a = np.deg2rad(angle)
    matrix = ([cos(a), -1 * sin(a), 0], [sin(a), cos(a), 0], [0, 0, 1])
    return np.matmul(matrix, points)


def rotate(points, anglex, angley, anglez):
    g = np.deg2rad(anglex)
    b = np.deg2rad(angley)
    a = np.deg2rad(anglez)
    matrix = ([cos(a) * cos(b), cos(a) * sin(b) * sin(g) - sin(a) * cos(g),
              cos(a) * sin(b) * cos(g) + sin(a) * sin(g)],
              [sin(a) * cos(b), sin(a) * sin(b) * sin(g) + cos(a) * cos(g),
              sin(a) * sin(b) * cos(g) - cos(a) * sin(g)],
              [-sin(b), cos(b) * sin(g), cos(b) * cos(g)])
    print(matrix)
    return np.matmul(matrix, points)


def sin(a):
    return np.sin(a)


def cos(a):
    return np.cos(a)


def skew(w):
    return np.array([[0, -w[2], w[1]], [w[2], 0, -w[0]], [-w[1], w[0], 0]])


def mat_exp(w, theta):
    return np.identity(3) + np.sin(theta) * w + (
            1 - np.cos(theta)) * np.matmul(w, w)


def mat_log(rot_mat):
    if np.array_equal(rot_mat, np.identity(3)):
        return 0
    elif np.trace(rot_mat) == 1:
        theta = np.pi
        w = 1.0 / math.sqrt(2.0 * (1 + rot_mat[0][0])) * np.array(
            [1 + rot_mat[0][0], rot_mat[1][0], rot_mat[2][0]])
        return w * theta
    else:  # ELSE theta = cos^-1(1/2(tr(R)-1)), w of a given form
        theta = np.arccos(.5 * (np.trace(rot_mat) - 1))
        w = 1.0 / (2.0 * np.sin(theta)) * (rot_mat - rot_mat.T)
        return w * theta

def print(self):
    print(self.matrix)
