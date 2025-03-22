import numpy as np

def make_diagonal(x):
	# Your code here
    sz = x.size
    ans = [[0 for i in range(sz)] for  j in range(sz)]
    for i in range (sz):
        ans[i][i] = x[i]

    return ans
