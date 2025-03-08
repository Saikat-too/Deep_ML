# Calculating a transform matrix of A where T and
# S given can't transform the matrix if T and S are not invertible
# So transform_A = T_inverse.(A.S)
import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]):
	a = np.array(A)
	t = np.array(T)
	s = np.array(S)
	det_t = np.linalg.det(t)
	det_s = np.linalg.det(s)
	if det_t == 0 or det_s == 0 :
		return -1
	t_inverse = np.linalg.inv(t);
	a_prime = np.dot(t_inverse,np.dot(a , s))
	return a_prime
