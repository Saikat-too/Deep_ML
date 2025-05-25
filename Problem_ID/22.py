import math

def sigmoid(z: float):
	#Your code here
	e = math.e
	e = e **(-z)
	result = 1 / (1 + e)
	result = f"{result:.4f}"
	return result
