# Q7. rotate values of a square matrix

def rotateMatrix1(matrix):
	# anti-clockwise
	n = len(matrix)
	# initalize 1-D matrix
	rotatedMatrix = [None] * n
	# initialize 2-D matrix
	for i in range(n):
		rotatedMatrix[i] = [None] * n
	# rotate
	# draw a matrix and assign values to see the process
	for row in range(n):
		for col in range(n):
			rotatedMatrix[n-col-1][row] = matrix[row][col]
	return rotatedMatrix

def rotateMatrix2(matrix):
	# clockwise
	n = len(matrix)
	# initalize 1-D matrix
	rotatedMatrix = [None] * n
	# initialize 2-D matrix
	for i in range(n):
		rotatedMatrix[i] = [None] * n
	# rotate
	for row in range(n):
		for col in range(n):
			rotatedMatrix[col][n-row-1] = matrix[row][col]
	return rotatedMatrix

if __name__ == "__main__":
	import sys
	A = [[1,2],[3,4]]
	print(A)
	print(rotateMatrix1(A))
	print(rotateMatrix2(A))
