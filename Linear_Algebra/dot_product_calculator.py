import numpy as np

def calculate_dot_product(vec1, vec2) -> float:
	"""
	Calculate the dot product of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	"""
	# Your code here
	#vec1 = vec1.reshape(-1 , 1)
	#vec2 = vec2.reshape(-1 , 1)
	sum = 0
	i = 0
	n = vec1.size
	for _ in range(n):
		sum += vec1[i] * vec2[i]
		i+=1



	return sum
