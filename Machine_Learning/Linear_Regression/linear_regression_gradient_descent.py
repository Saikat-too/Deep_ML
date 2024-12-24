import numpy as np
def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
	m, n = X.shape
	# intercept / slop
	theta = np.zeros((n, 1))
	# learning rate of the model
	learning_rate = alpha
	for i in range(iterations):
		# Calculate the predicted value
		y_pred = np.dot( X , theta)
		# errors
		errors = y_pred - y.reshape(-1 , 1)
		# derivative
		theta_derivatives = np.dot(X.T , errors) / m
		# gradient descent
		theta = theta - learning_rate * theta_derivatives

	return np.round(theta.flatten() , 4)
