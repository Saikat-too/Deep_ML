import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	# Your code here\
    len , _ = X.shape
    len_range = (len+batch_size-1) // batch_size
    ans = []
    for i in range(len_range):
        X_slice = X[batch_size * i : min(batch_size * (i+1) , len)]
        if y is not None :
            y_slice = y[batch_size * i : min(batch_size * (i+1),len)]
            ans.append((X_slice , y_slice))
        else :
            ans.append(X_slice)
	return ans
