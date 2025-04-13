import numpy as np

def k_fold_cross_validation(X: np.ndarray, y: np.ndarray, k=5, shuffle=True, random_seed=None):
    """
    Implement k-fold cross-validation by returning train-test indices.
    """

    result = []
    fold_size = X.size // k
    start = 0
    for i in range (k):
        if not shuffle:
          test_indices = X[i*fold_size : (i+1)*fold_size]
          train_indices  = np.concatenate([X[:i*fold_size] , X[(i+1)*fold_size:]])
          result.append((train_indices , test_indices))
        else:
            np.random.seed(random_seed)
            indices = np.random.permutation(X)
            # print(X)
            test_start = start
            test_end   = start + fold_size
            test_indices = indices[test_start:test_end]
            train_indices = np.concatenate([indices[:test_start],indices[test_end:]])
            result.append((train_indices , test_indices))
            start = test_end


    return result
