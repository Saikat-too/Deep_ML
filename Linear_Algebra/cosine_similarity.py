
import numpy as np

def cosine_similarity(v1, v2):
	# Implement your code here
	if v1.shape != v2.shape :
		return

	v1_sum = 0.0
	v2_sum = 0.0
	v1_v2_sum = 0.0
	for a in v1:
		v1_sum += a * a

	for b in v2:
		v2_sum += b * b

	for a , b in zip(v1 , v2):
		v1_v2_sum += a * b



	v1_sqrt =  v1_sum ** 0.5
	v2_sqrt =  v2_sum ** 0.5
	if v1_sqrt == 0 or v2_sqrt == 0 :
		return

	cos_theta = (v1_v2_sum) / ((v1_sqrt) * (v2_sqrt))
	return np.round(cos_theta ,decimals = 3)
