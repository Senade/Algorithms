def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums)//2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


def merge(nums1, nums2):
    i, j = 0, 0
    merged = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    while i < len(nums1):
        merged.append(nums1[i])
        i += 1

    while j < len(nums2):
        merged.append(nums2[j])
        j += 1
        
    return merged


def main():
    try:
        assert merge_sort([1, 3, 8, 2, 9, 2, 5, 6]) == \
            [1, 2, 2, 3, 5, 6, 8, 9]
    except AssertionError as e:
        print("Tests failed")
        raise e
    print("Tests passed")


if __name__ == "__main__":
    main()
