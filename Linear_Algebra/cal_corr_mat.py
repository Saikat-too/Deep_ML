
"""

Standardization transforms a dataset so that each feature has a mean of 0 and standard deviation of 1 .
Mathematically , for a feature X , the standardized value Z for each data point x is calculated as Z = (data - mean) / standard deviation.
The intution here is about comparability and fairness across feature.

Normalization , specifically min-max normalization , rescales a feature to fit within a fixed range , typically [0 , 1].
The formula is Xnorm = (data - min(X)) / (max(X) - min(X))


"""


import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# calculate mean and standard deviation
    mean = np.mean(data , axis=0)
    std_dev = np.std(data , axis=0)

    # standardized_data

    standardized_data = np.round((data - mean)/std_dev , 4)

    # calculate min and max
    min_val = np.min(data , axis=0)
    max_val = np.max(data , axis =0)

    # normalized_data
    normalized_data = np.round((data - min_val)/(max_val - min_val) , 4)

	return standardized_data, normalized_data
