def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	means = []

	if mode == 'row' :
		for i in range(len(matrix)):
			sum = 0.0
			for j in range(len(matrix[0])):
				sum += matrix[i][j]
			means.append(sum / len(matrix[0]))

	if mode == 'column':

		for i in range(len(matrix[0])):
			sum = 0.0
			for j in range(len(matrix)):
				sum += matrix[j][i]
			means.append(sum / len(matrix))



	return means
