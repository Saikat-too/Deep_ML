import numpy as np
def matrix_dot_vector(a , b):
	a = np.array(a)
	b = np.array(b)
	b = b.reshape(-1 , 1)
	a_row , a_column = a.shape
	b_row , b_column = b.shape
	if a_column!=b_row:
		return -1
	c = np.zeros((a_row , b_column))
	# c = np.reshape(-1 , 1)
	for i in range(a_row):
		for j in range(b_column):
			for k in range(b_row):
				c[i , j] += a[i , k] * b[k , j]

	return c.flatten()
