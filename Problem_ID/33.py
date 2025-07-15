import numpy as np

def get_random_subsets(X, y, n_subsets, replacements=True, seed=42):
	np.random.seed(seed)
	size = int(np.ceil(y.size / n_subsets))
	subsets = []
	for i in range(n_subsets):
		indices = np.random.choice(X.shape[0] ,size=size , replace=replacements )
		X_subset = X[indices]
		y_subset = y[indices]
	    # subsets.append((X_subset , y_subset))
	    subsets.append(X_subset.tolist())
	    subsets.append(y_subset.tolist())


	return subsets
