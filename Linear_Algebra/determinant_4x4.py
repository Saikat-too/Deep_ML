  # Need to find the determinant of a 4x4 matrix using Laplace's Expansion .

def determinant_3x3(a) -> float:
	return(a[0][0] * (a[1][1] * a[2][2] - a[2][1]*a[1][2])-a[1][0] * (a[0][1] * a[2][2] - a[0][2] * a[2][1]) + a[2][0] * (a[0][1] * a[1][2] - a[1][1] * a[0][2]))

def determinant_4x4(matrix: list[list[int|float]]) -> float:
	# Your recursive implementation here
	total = 0
	column = 0
	for element  in (matrix[0]):
		k = [x[:column] + x[column+1:] for x in matrix[1:]]
		s = 1 if column % 2 == 0 else -1
		total += s * element * determinant_3x3(k)
		column+=1
	return total
