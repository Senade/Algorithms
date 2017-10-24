def counting_sort(nums):
    bookkeeping_array = [0] * (max(nums) + 1)
    sorted_nums = []
    for num in nums:
        bookkeeping_array[num] += 1
    for num, freq in enumerate(bookkeeping_array):
        sorted_nums.extend([num] * freq)
    return sorted_nums


def main():
    try:
        assert counting_sort([1, 3, 8, 2, 9, 2, 5, 6]) == \
            [1, 2, 2, 3, 5, 6, 8, 9]
    except AssertionError as e:
        print("Tests failed")
        raise e
    print("Tests passed")


if __name__ == "__main__":
    main()
