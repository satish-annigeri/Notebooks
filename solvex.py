import numpy as np
r = 1
A = np.array([[5.0, 2*r, r], [3, 6, 2*r-1], [2, r-1, 3*r]])
b = np.array([2.0, 3, 5])
det_A = np.linalg.det(A)
x = np.linalg.solve(A, b)
