def binary_search_recur(nums, k):
	a, b = 0, len(nums) - 1
	return binary_search_recur_helper(nums, k, a, b)


def binary_search_recur_helper(nums, k, start, end):
	mid = start + (end - start)//2
	if nums[mid] == k:
		return mid
	elif k > nums[mid]:
		return binary_search_recur_helper(nums, k, k+1, end)
	else:
		return binary_search_recur_helper(nums, k, start, k-1)


def binary_search_iter(nums, k):
	a, b = 0, len(nums) - 1
	while(a <= b):
		mid = a + (b - 1)//2
		if nums[mid] == k:
			return mid
		elif k > nums[mid]:
			a = k + 1
		else:
			b = k - 1
	return None


def main():
    try:
        assert binary_search_iter([1, 2, 2, 3, 5, 6, 8, 9], 2) == 3
        assert binary_search_recur([1, 2, 2, 3, 5, 6, 8, 9], 2) == 3
    except AssertionError as e:
        print("Tests failed")
        raise e
    print("Tests passed")


if __name__ == "__main__":
    main()