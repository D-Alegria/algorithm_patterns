"""
    Target Sum (hard)
    You are given a set of positive numbers and a target sum ‘S’.
    Each number should be assigned either a ‘+’ or ‘-’ sign.
    We need to find the total ways to assign symbols to make the sum of the numbers equal to the target ‘S’.

    Example 1:#
    Input: {1, 1, 2, 3}, S=1
    Output: 3
    Explanation: The given set has '3' ways to make a sum of '1': {+1-1-2+3} & {-1+1-2+3} & {+1+1+2-3}

    Example 2:#
    Input: {1, 2, 7, 1}, S=9
    Output: 2
    Explanation: The given set has '2' ways to make a sum of '9': {+1+2+7-1} & {-1+2+7+1}
"""


def memoization_find_target_subsets(nums, s):
    total = sum(nums)
    memo = [[None for __ in range(-total, total + 1)] for _ in range(len(nums))]
    return process(nums, s, 0, memo)


def process(nums, s, currentIndex, memo):
    if currentIndex >= len(nums):
        if s == 0:
            return 1
        else:
            return 0

    if memo[currentIndex][s] is not None:
        return memo[currentIndex][s]
    add = process(nums, s + nums[currentIndex], currentIndex + 1, memo)
    sub = process(nums, s - nums[currentIndex], currentIndex + 1, memo)
    memo[currentIndex][s] = add + sub
    return memo[currentIndex][s]


def tabulation_find_target_subsets(nums, s):
    total = sum(nums)
    table = [[0 for __ in range(-total, total + 1)] for _ in range(len(nums))]
    pass

if __name__ == '__main__':
    print("Total ways memoization: " + str(memoization_find_target_subsets([1, 1, 2, 3], 1)))
    print("Total ways memoization: " + str(memoization_find_target_subsets([1, 2, 7, 1], 9)))
