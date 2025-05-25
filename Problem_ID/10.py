def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
    size = len(vectors)

    result = [[0 for i in range(size)] for j in range(size)]

    means = []

    for i in range(size):
        mean_sum = 0
        mean = 0
        for j in range(len(vectors[0])):
            mean_sum+= vectors[i][j]
        mean = mean_sum / len(vectors[0])
        means.append(mean)


    for k in range(size):
        for l in range(size):
            cov_sum = 0
            cov = 0
            for m in range(len(vectors[0])):
                cov_sum += (vectors[k][m] - means[k]) * (vectors[l][m] - means[l])
            cov = cov_sum / (len(vectors[0]) - 1)
            result[k][l] = cov


	return result
