COUNT = 0

def n_queens(row, n, column, diagonal1, diagonal2):
	global COUNT
	if row == n:
		COUNT += 1
	else:
		for col in range(n):
			if column[col] or diagonal1[row+col] or diagonal2[row-col+n-1]:
				continue
			column[col] = diagonal1[row+col] = diagonal2[row-col+n-1] = 1
			n_queens_1(row+1, n, column, diagonal1, diagonal2)
			column[col] = diagonal1[row+col] = diagonal2[row-col+n-1] = 0

def main():
	n = 16
	n_queens(0, n, [0]*n, [0]*(2*n-1), [0]*(2*n-1))
	print(COUNT)


if __name__ == '__main__':
	main()


