# O(N) solution - Kadane's algorithm
def maxsubarray(nums):
    sum = 0
    best = float("-inf")
    for n in nums:
        sum = max(n, sum + n)
        best = max(best, sum)
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
