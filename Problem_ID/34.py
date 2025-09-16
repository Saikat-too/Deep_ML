import numpy as np

def to_categorical(x, n_col=None):

	if n_col == None:
		max_number = 0
		for num in x:
			if max_number < num :
				max_number = num

		n_col = max_number + 1

	n_row  = x.shape[0]
	result = np.zeros((n_row , n_col))

	for index in range(n_row):
		result[index][x[index]] = 1

	return result
