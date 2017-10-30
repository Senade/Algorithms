# consider a problem where we are given n numbers a1,a2,...,an
# and our task is to find a value x that minimizes the sum
# |a1 −x|^c +|a2 −x|^c +···+|an −x|^c.
# Solve for c = 1 and c = 2

import statistics as stats


def minimum_sum_c_1(nums):
	# The median is an optimal choice, because if x is smaller than 
	# the median, the sum becomes smaller by increasing x, and if 
	# x is larger then the median, the sum becomes smaller by 
	# decreasing x. Hence, the optimal solution is that x is the 
	# median. If n is even and there are two medians, both medians 
	# and all values between them are optimal choices.
    x = stats.median(nums)
    return sum([abs(n - x) for n in nums])


def minimum_sum_c_2(nums):
	# Expanding, and differentiating the quadratic equation
	# w.r.t x gives the mean
    x = stats.mean(nums)
    return sum([abs(n - x)**2 for n in nums])


def minimum_sum(nums, c):
    if c == 1:
        return minimum_sum_c_1(nums)
    elif c == 2:
        return minimum_sum_c_2(nums)
    else:
        return None


def main():
    nums = [1, 2, 9, 2, 6]
    print(minimum_sum(nums, 1))
    print(minimum_sum(nums, 2))


if __name__ == '__main__':
    main()
