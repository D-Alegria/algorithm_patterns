"""
    Count of Subset Sum (hard)#
    Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.

    Example 1:#
    Input: {1, 1, 2, 3}, S=4
    Output: 3
    The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
    Note that we have two similar sets {1, 3}, because we have two '1' in our input.

    Example 2:#
    Input: {1, 2, 7, 1, 5}, S=9
    Output: 3
    The given set has '3' subsets whose sum is '9': {2, 7}, {1, 7, 1}, {1, 2, 1, 5}

"""


def memoization_count_subsets(nums, total):
    table = [[-1 for __ in range(total + 1)] for _ in range(len(nums))]
    return process(nums, total, 0, table)


def process(nums, total, currentIndex, table):
    if total == 0:
        return 1

    if total < 0 or currentIndex >= len(nums):
        return 0

    if table[currentIndex][total] > -1:
        return table[currentIndex][total]
    table[currentIndex][total] = process(nums, total - nums[currentIndex], currentIndex + 1, table) + \
                                 process(nums,
                                         total,
                                         currentIndex + 1,
                                         table)
    return table[currentIndex][total]


def tabulation_count_subsets(nums, total):
    table = [[0 for __ in range(total + 1)] for _ in range(len(nums))]
    n = len(nums)

    for i in range(n):
        table[i][0] = 1

    table[0][nums[0]] = 1

    for i in range(1, n):
        for t in range(1, total + 1):
            withNum = 0 if t < nums[i] else table[i - 1][t - nums[i]]
            withOutNum = table[i - 1][t]
            table[i][t] = withNum + withOutNum
    return table[-1][-1]


"""
    DFS
    S = Sum
    N = no of items

    time = O(2^N)
    space = o(N)

    After memoization
    time = O(N*S)
    space = O(N*S)

    Tabulation
    time = O(N*S)
    space = O(N*S)
"""

if __name__ == '__main__':
    print("Total number of subsets " + str(memoization_count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(memoization_count_subsets([1, 2, 7, 1, 5], 9)))
    print("Total number of subsets " + str(tabulation_count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(tabulation_count_subsets([1, 2, 7, 1, 5], 9)))
