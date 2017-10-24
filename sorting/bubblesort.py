def bubble_sort(nums):
    length_nums = len(nums)
    for i in range(length_nums):
        for j in range(length_nums - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def main():
    try:
        assert bubble_sort([1, 3, 8, 2, 9, 2, 5, 6]) == \
            [1, 2, 2, 3, 5, 6, 8, 9]
    except AssertionError as e:
        print("Tests failed")
        raise e
    print("Tests passed")


if __name__ == "__main__":
    main()
