import matplotlib.pyplot as plt
import numpy as np
import time
from IPython.display import display, clear_output
import Matrices.frame as fr

#units are in mm

delay = 1

L2 = fr.linkage("L2", [[[0],[0],[0]], [[0],[0],[105]]])
R3 = fr.rotateJoint("R3", [-1,0,0], [[0],[0],[0]])
L2.addFrame(R3)
R2 = fr.rotateJoint("R2", [1,0,0], [[0],[0],[0]])
R2.addFrame(L2)
L1 = fr.linkage("L1", [[[0],[0],[0]], [[0], [0], [80]]])
L1.addFrame(R2)
R1 = fr.rotateJoint("R1", [0,0,1], [[0],[0],[0]])
R1.addFrame(L1)
R3.setParent(L2)
L2.setParent(R2)
R2.setParent(L1)
L1.setParent(R1)

data = R1.getPoints()

#print(data)

fig = plt.figure()

ax = fig.add_subplot(projection='3d')
eps = 1e-16
ax.axes.set_xlim3d(left=-10.-eps, right=150+eps)
ax.axes.set_ylim3d(bottom=-10.-eps, top=150+eps) 
ax.axes.set_zlim3d(bottom=-10.-eps, top=300+eps) 
for d in data:
    ax.scatter(d[0][0], d[1][0], d[2][0], marker='o')
display(fig)
clear_output(wait = True)
plt.pause(delay)
plt.show()
