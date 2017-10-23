# O(N^2) solution
def maxsubarray(nums):
    best = float("-inf")
    n = len(nums)
    for a in range(n):
        sum = 0
        for b in range(a, n):
            sum += nums[b]
            best = max(sum, best)
    return best


def main():
    try:
        assert maxsubarray([-1, 2, 4, -3, 5, 2, -5, 2]) == 10
    except AssertionError as e:
        print("Tests failed")
        raise e
    print("Tests passed")


if __name__ == "__main__":
    main()
