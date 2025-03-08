# Doing matrix multiplication here with matrixes and the equation
# C(i , j) = sum from i to a_column (A[i , k] * B[k , j])
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]]):
	a_row = len(a)
	a_column = len(a[0])
	b_row  = len(b)
	b_column = len(b[0])
	if a_column != b_row :
		return -1

	c = [[0 or 0.0 for x in range(b_column)] for y in range(a_row)]
	for i in range(a_row):
		for j in range(b_column):
			for k in range(b_row):
				c[i][j] += a[i][k] * b[k][j]
	return c
