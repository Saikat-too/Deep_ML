def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	columns = len(matrix)
	rows    = len(matrix[0])
	result = [[0 for x in range(columns)]  for y in range(rows)]
	for i in range (len(matrix)):
		for j in range(len(matrix[i])):
			result[i][j] = scalar * matrix[i][j]
	return result
