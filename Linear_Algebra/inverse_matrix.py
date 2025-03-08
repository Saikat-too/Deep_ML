# Inversion of matrix in matrix A = (a b) where inverse is = 1/(ad-bc)(d -c)
#                                   (c d)                             (-b a)

import numpy as np
def inverse_2x2(matrix: list[list[float]]):
	a = matrix[0][0]
	b = matrix[0][1]
	c = matrix[1][0]
	d = matrix[1][1]
	det_mat = a*d - b*c
	if det_mat == 0 :
		return None


	matrix[0][0] = d
	matrix[0][1] = -b
	matrix[1][0] = -c
	matrix[1][1] = a


	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			matrix[i][j] *= 1/det_mat

	return np.round(matrix , 1)
