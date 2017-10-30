def search(n, chosen, permutations):
	if len(permutations) == n:
		print(permutations)
	else:
		for i in range(n):
			if chosen[i]: continue
			chosen[i] = True
			permutations.append(i)
			search(n, chosen, permutations)
			chosen[i] = False
			permutations.pop()


def main():
	n = 3
	search(n, [0] * n, [])


if __name__ == '__main__':
	main()


	