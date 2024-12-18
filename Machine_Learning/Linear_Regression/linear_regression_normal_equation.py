import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	X = np.array(X)
	y = np.array(y).reshape(-1 , 1)
	X_transpose = X.T
	theta = np.linalg.inv(X_transpose.dot(X)).dot(X_transpose).dot(y)
	theta = np.round(theta , 4).flatten().tolist()
	return theta


# print(linear_regression_normal_equation([[1,1] , [1,2] , [1,3]] , [1,2,3]))
# print(linear_regression_normal_equation([[1,3,4] , [1,2,5] , [1,3,2]] , [1,2,1]))
