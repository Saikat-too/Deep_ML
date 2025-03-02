def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	# To find eigenvalues first need to find the trace of the
	# matrix and find mean of it then find the determinant of
	# the matrix to find the ultimate eigen values
	trace = 0.0
	for i in range(len(matrix)):
		trace += matrix[i][i]
	mean = trace / 2
	product = matrix[0][0] * matrix[1][1] - matrix[0][1]*matrix[1][0]

	eigenvalues1 = mean + (mean*mean - product)**0.5
	eigenvalues2 = mean - (mean*mean - product)**0.5
	eigenvalues = []
	eigenvalues.append(eigenvalues1)
	eigenvalues.append(eigenvalues2)
	return eigenvalues
