import numpy as np
import matplotlib.pyplot as plt
import math

L1 = 3.0
L2 = 2.0
L3 = 1.0

M = np.matrix([[1,0,0,6],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
#x = L1cos(t1) + L2cos(t1 + t2) + L3cos(t1 + t2 + t3)
#y = L1sin(t1) + L2sin(t1 + t2) + L3sin(t1 + t2 + t3)
#phi = t1+t2+t3
#tan(t) = y/x = m

def invkin(px, py, phi):
	bx = px - np.cos(phi) * L3
	by = py - np.sin(phi) * L3

	gamma = math.atan2(by, bx)
	beta = np.arccos((L1 ** 2 + L2 ** 2- bx ** 2 - by ** 2)/(2 * L1 * L2))
	alpha = np.arccos((bx ** 2 + by ** 2 + L1 ** 2 - L2 ** 2)/(2 * L1 * math.sqrt(bx ** 2 + by ** 2)))

	# theta values
	t1r = gamma - alpha
	t1l = gamma + alpha
	t2r = np.pi - beta
	t2l = beta - np.pi

	t3r = phi - t1r - t2r
	t3l = phi - t1l - t2l

	x0 = 0
	y0 = 0

	x1r = x0 + np.cos(t1r) * L1
	x1l = x0 + np.cos(t1l) * L1

	x2r = x1r + np.cos(t1r + t2r) * L2
	x2l = x1l + np.cos(t1l + t2l) * L2

	x3r = x2r + np.cos(t1r + t2r + t3r) * L3
	x3l = x2l + np.cos(t1l + t2l + t3l) * L3

	y1r = y0 + np.sin(t1r) * L1
	y1l = y0 + np.sin(t1l) * L1

	y2r = y1r + np.sin(t1r + t2r) * L2
	y2l = y1l + np.sin(t1l + t2l) * L2

	y3r = y2r + np.sin(t1r + t2r + t3r) * L3
	y3l = y2l + np.sin(t1l + t2l + t3l) * L3

	Xr = [x0, x1r, x2r, x3r]
	Xl = [x0, x1l, x2l, x3l]

	Yr = [y0, y1r, y2r, y3r]
	Yl = [y0, y1l, y2l, y3l]

	print(t1r, t2r, t3r)
	print(t1l, t2l, t3l)

	fig, ax = plt.subplots()
	fig.set_size_inches(6, 6)
	plt.title("Exercise 6.1")
	plt.plot(Xr, Yr, '--', dashes=(5, 1), label='right solution')
	plt.plot(Xl, Yl, '--', dashes=(4, 2), label='left solution')
	plt.plot(px, py, 'ro')
	ax.legend()
	plt.show()


invkin(4, 2, 0)

