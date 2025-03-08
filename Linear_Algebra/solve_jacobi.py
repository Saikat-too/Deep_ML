# solving  a (Ax = b)linear system  using jacobi method

import numpy as np
def solve_jacobi(a: np.ndarray, b: np.ndarray, n: int) -> list:
	size = b.size
	x_old = np.zeros(size)
	x_new = np.zeros(size)
	for k in range(n) :
		for i in range(size):
			element_sum = 0
			for j in range(size):
				if i != j :
					element_sum = np.round(element_sum + a[i][j] * x_old[j] , 4)
			x_new[i] = np.round((b[i] - element_sum) / a[i][i] , 4)
		x_old = x_new.copy()

	return x_new.tolist()
