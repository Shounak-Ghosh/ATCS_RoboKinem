import numpy as np
import rotation as rotate


p = np.array([1/np.sqrt(3), -1/np.sqrt(6), 1/np.sqrt(2)])
p2 = rotate.rotate(p, 30, 135, -120)
p = rotate.x(p, 30)
p = rotate.y(p, 135)
p = rotate.z(p, -120)
print(p)
print(p2)
