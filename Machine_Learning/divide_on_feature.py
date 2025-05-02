import numpy as np

def divide_on_feature(X, feature_i, threshold):
	"""
	Divide the dataset based on whether the value of a specified feature is greater than or equal to a given threshold.

	Args :
		1. X(numpy.ndarray) : Input dataset , 2d array where rows are samples and columns are features .
		2. feature_i(int) : Index  of the column of the feature to look for to compare against threshold .
		3. threshold(int) : Threshold value for spliting the dataset  .
	Return  :
		Two numpy arrays(X_ge , X_lt)
		  - X_ge : Subset of X where the value >=threshold
		  - X_lt : Subset of X where the value < threshold
	"""

	# Create boolean mask for sample where feature_i >= threshold

	mask = X[: , feature_i] >= threshold

	# Split dataset using mask .
	X_ge = X[mask]
	X_lt = X[~mask]

	return X_ge , X_lt
