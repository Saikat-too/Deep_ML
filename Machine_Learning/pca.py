"""
PCA provides a roadmap for how to reduce a complex data set to lower dimension to reveal something hidden , simplified structures that often
underlie it . The goal of principal component analysis is to identify the most meaningful basis to re-express a data set . The hope is that new
basis will reduce noise and reveal hidden structure . PCA finds a linear data transformation that projects the data into a new coordinate system
with a fewer dimensions . To capture the most variations in the original data , the projection is done by finding the so called principal
components , eigenvectors of the data's covariance matrix and multiplying data matrix with  a subset of components.

Things to do --->
1. Centering the data : PCA is affected by the scale of the data , so the first things to do is to subtract the mean of Each
feature of the dataset , thus ensuring that all the features have a mean of equal to 0.

2. Calculate covariance matrix : Now , we have to calculate the covariance matrix to capture how each pair of features in the data varies together, If the dataset has n features,
the resulting covariance matrix will have n x n shape.

3. Eigenvalue Decomposition : Next , we have to perform the eigenvalue decomposition of the covariance matrix.

4. Selecting the Principal Components : The eigenvalues quantify the data's variance in the direction of its corresponding eigenvector.Thus , we sort the eigenvalues in descending
order and keep only the top n required principal components.



"""
import numpy as np
def pca(data: np.ndarray, k: int) -> np.ndarray:
    """
    Perform PCA on the input dataset and return principal components, projected data, and eigenvalues.

       Args:
           data: Input data (n x p array , n observations , p features)
           k: Number of principal components to return

       Returns:
           principal_components: Top k eigenvectors (p x k)
    """
	data = data.astype(np.float64)
	# Data Centering
	data_mean = np.mean(data , axis = 0)
	data_std  = np.std(data , axis = 0 ,ddof=0)
	data = (data - data_mean) / data_std
	# Calculate covariance matrix
	cov_matrix = np.cov(data.T)

	# Calculate eigenvalues and eigenvactors
	ei_values , ei_vectors = np.linalg.eig(cov_matrix)
	# Sort eigenvalues and vectors
	sort_idx = np.argsort(ei_values)[::-1]
	ei_values = ei_values[sort_idx]
	ei_vectors = ei_vectors[: ,sort_idx]
	# Store Principal Component Analysis
	principal_components = ei_vectors[:,:k]
	return np.round(principal_components, 4)
