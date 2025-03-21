def det_C(C) -> float:
	if len(C) == 1:
		return C[0][0]
	if len(C) == 2 :
		return C[0][0] * C[1][1] - C[0][1] * C[1][0]
	if len(C) == 3 :
		return (C[0][0] * (C[1][1] * C[2][2] - C[1][2] * C[2][1])
				-C[0][1] * (C[1][0] * C[2][2] - C[1][2] * C[2][0]) + C[0][2] * (C[1][0] * C[2][1] - C[1][1] * C[2][0]))

def mat_adj(C , C_adj):
	for i in range(len(C)):
		for j in range(len(C[0])):
			minor =[[C[x][y] for y in range(len(C)) if y!=j] for x in range(len(C)) if x!=i]
			sign = 1 if (i+j) % 2 == 0 else -1
			C_adj[i][j] = sign * det_C(minor)

def transform_basis(B, C):
	det = det_C(C)
	if det == 0 :
		return None
	det = 1/det
	C_adj = [[0] * len(C) for _ in range(len(C))]
	mat_adj(C , C_adj)
	C_inv = [[C_adj[j][i] * det for j in range(len(C))] for i in range (len(C))]
	P = [[sum(C_inv[i][k] * B[k][j] for k in range(len(C[0]))) for j in range(len(C[0]))] for i in range(len(C))]

	return [[round(val, 4) for val in row] for row in P]
