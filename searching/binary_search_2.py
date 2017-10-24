def binary_search(nums, x):
	n = len(nums)
	k, b = 0, n//2
	print("b = {}".format(b))
	while b >= 1:
		while k+b < n and nums[k+b] <= x:
			k += b
		b = b//2
	print("K = {}".format(k))
	if nums[k] == x:
		return k
	else:
		return None


def main():
    try:
        assert binary_search([1, 3, 8, 2, 9, 2, 5, 6], 2) == 3
    except AssertionError as e:
        print("Tests failed")
        print(binary_search([1, 3, 8, 2, 9, 2, 5, 6], 2))
        raise e
    print("Tests passed")


if __name__ == "__main__":
    main()