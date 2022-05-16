"""
    Given a set of positive numbers, determine if a subset exists whose sum is equal to a given number ‘S’.

    Example 1:
    Input: {1, 2, 3, 7}, S=6
    Output: True
    The given set has a subset whose sum is '6': {1, 2, 3}

    Example 2:
    Input: {1, 2, 7, 1, 5}, S=10
    Output: True
    The given set has a subset whose sum is '10': {1, 2, 7}

    Example 3:
    Input: {1, 3, 4, 8}, S=6
    Output: False
    The given set does not have any subset whose sum is equal to '6'.
"""


def memoization_can_partition(nums, target):
    def process(target, currentIndex=0, memo=None):
        if memo is None:
            memo = [[-1 for _ in range(target + 1)] for __ in range(len(nums))]
        if target == 0:
            return True

        if target < 0 or currentIndex >= len(nums):
            return False

        if memo[currentIndex][target] != -1:
            return memo[currentIndex][target]

        return process(target, currentIndex + 1, memo) or process(target - nums[
            currentIndex], currentIndex + 1, memo)

    return True if process(target, 0) == 1 else False


def tabulation_can_partition(nums, target):
    n = len(nums)
    table = [[False for i in range(target + 1)] for __ in range(n)]

    for i in range(n):
        table[i][0] = True

    if nums[0] <= target:
        table[0][nums[0]] = True

    for i in range(1, n):
        for t in range(1, target + 1):
            withNum = table[i - 1][t - nums[i]] if nums[i] <= t else False
            withOutNum = table[i - 1][t]

            table[i][t] = withNum or withOutNum

    return table[-1][-1]


"""
    DFS
    T = target
    N = no of items

    time = O(2^N)
    space = o(N)

    After memoization
    time = O(N*T)
    space = O(N*T)

    Tabulation
     time = O(N*T)
    space = O(N*T)
"""

if __name__ == '__main__':
    print("Can partition memoization: " + str(memoization_can_partition([1, 2, 3, 7], 6)))
    print("Can partition memoization: " + str(memoization_can_partition([1, 2, 7, 1, 5], 10)))
    print("Can partition memoization: " + str(memoization_can_partition([1, 3, 4, 8], 6)))
    print("-----------------------------------------------------")
    print("Can partition tabulation: " + str(tabulation_can_partition([1, 2, 3, 7], 6)))
    print("Can partition tabulation: " + str(tabulation_can_partition([1, 2, 7, 1, 5], 10)))
    print("Can partition tabulation: " + str(tabulation_can_partition([1, 3, 4, 8], 6)))
