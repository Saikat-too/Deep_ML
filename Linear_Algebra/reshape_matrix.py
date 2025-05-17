import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	# Write your code here and return a python list after reshaping by using numpy's tolist() method

	elements = []

	row = len(a)
	column = len(a[0])

	for i in range(row):
		for j in range(column):
			elements.append(a[i][j])


	reshaped_matrix = []

	if row * column == new_shape[0] * new_shape[1]:
		reshaped_matrix = [[0] * new_shape[1] for _ in range(new_shape[0])]
		ind = 0
		for i in range(new_shape[0]):
			for j in range(new_shape[1]):
				reshaped_matrix[i][j] = elements[ind]
				ind+=1



	return reshaped_matrix
