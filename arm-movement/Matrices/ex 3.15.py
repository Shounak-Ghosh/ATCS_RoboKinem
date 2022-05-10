import numpy as np
import frame as fr

test = fr.Frame("test", np.array([[[0], [1], [0]], [[0], [2], [0]]]))
test.setOrigin([[0],[0],[0]])
a = np.deg2rad(90)
b = np.deg2rad(45)
g = np.deg2rad(0)
#test.rotateWithMatrix((np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])))
f2 = test.rotateAboutAxis([1,0,0], a)
f3 = test.rotateAboutAxis([0,1,0], b)
f4 = test.rotateAboutAxis([0,0,1], g)

print("a)")
print(f4)
#test.print()

print("b)")
print(f3.rotateAboutAxis([0,1,0]), g)

print("c)")
arr_ab = np.array([[1 / 2 ** .5, -1 / 2 ** .5, 0, -1], 
             [1 / 2 ** .5, 1 / 2 ** .5, 0, 0],
             [0, 0, 1, 1], 
             [0, 0, 0, 1]])

arr_cb = np.array([[1 / 2 ** .5, 0, 1 / 2 ** .5, 0], 
                   [0, 1, 0, 1],
                   [-1 / 2 ** .5, 0, 1 / 2 ** .5, 0], 
                   [0, 0, 0, 1]])

arr_ba = np.linalg.inv(arr_ab)
arr_ca = np.matmul(arr_cb, arr_ba)
print(arr_ca)


