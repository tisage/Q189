# Q8. Zero out a M*N matrix

def zeroOut(matrix):
	n = len(matrix)
	m = len(matrix[0])

	# use two lists to record zero element location
	zeroRow, zeroCol = [], []

	for row in range(n):
		for col in range(m):
			if matrix[row][col] == 0:
				zeroRow.append(row)
				zeroCol.append(col)
				# because zero out the whole row and col
				# skip this row and go to the next row
				break

	# set zero values on matrix
	for row in zeroRow:
		for i in range(m):
			matrix[row][i] = 0

	for col in zeroCol:
		for i in range(n):
			matrix[i][col] = 0

	return matrix

if __name__ == "__main__":
	import sys
	A = [[0,2],[3,4]]
	B = [[2,0,5],[3,2,0],[1,1,1]]

	print(A)
	print(zeroOut(A))
	print('')
	print(B)
	print(zeroOut(B))