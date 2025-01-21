import numpy as np
def transpose_matrix(a):
	a = np.array(a)
	a_row , a_column = a.shape
	b = np.zeros((a_column , a_row))
	for i in range(a_row):
		for j in range(a_column):
			b[j][i] = a[i][j]

	return b
