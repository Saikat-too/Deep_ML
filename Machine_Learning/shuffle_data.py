import numpy as np

def shuffle_data(X, y, seed=None):
	if seed != None :
        np.random.seed(seed)

    indices = np.arange(X.shape[0])
    np.random.shuffle(indices)
    X = X[indices]
    y = y[indices]



    return X , y
