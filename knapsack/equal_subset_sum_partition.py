"""
    Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both subsets is equal.

    Example 1:
    Input: {1, 2, 3, 4}
    Output: True
    Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}

    Example 2:
    Input: {1, 1, 3, 4, 7}
    Output: True
    Explanation: The given set can be partitioned into two subsets with equal sum: {1, 3, 4} & {1, 7}

    Example 3:
    Input: {2, 3, 4, 6}
    Output: False
    Explanation: The given set cannot be partitioned into two subsets with equal sum.
"""


def memoization_can_partition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False

    n = len(nums)
    memo = [[-1 for _ in range(int(total / 2) + 1)] for _ in range(n)]

    def process(target, currentIndex):
        if target == 0:
            return 1

        if target < 0 or currentIndex >= n:
            return 0

        if 0 <= memo[currentIndex][target] <= 1:
            return memo[currentIndex][target]

        if process(target - nums[currentIndex], currentIndex + 1) == 1:
            memo[currentIndex][target] = 1
            return 1
        memo[currentIndex][target] = process(target, currentIndex + 1)
        return memo[currentIndex][target]

    return True if process(int(total / 2), 0) == 1 else False


def tabulation_can_partition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False

    n = len(nums)
    table = [[False for _ in range(int(total / 2) + 1)] for _ in range(n)]

    for i in range(n):
        table[i][0] = True

    table[0][nums[0]] = True

    for i in range(1, n):
        for s in range(1, int(total / 2) + 1):
            withOutNum = table[i - 1][s]
            withNum = table[i - 1][s - nums[i]] if nums[i] <= s else False

            table[i][s] = withNum or withOutNum
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
    print("Can partition memoization: " + str(memoization_can_partition([1, 2, 3, 4])))
    print("Can partition memoization: " + str(memoization_can_partition([1, 1, 3, 4, 7])))
    print("Can partition memoization: " + str(memoization_can_partition([2, 3, 4, 6])))
    print("Can partition memoization: " + str(memoization_can_partition([1, 1, 3, 4, 7, 3, 5, 18, 19, 23])))
    print("-----------------------------------------------------")
    print("Can partition tabulation: " + str(tabulation_can_partition([1, 2, 3, 4])))
    print("Can partition tabulation: " + str(tabulation_can_partition([1, 1, 3, 4, 7])))
    print("Can partition tabulation: " + str(tabulation_can_partition([2, 3, 4, 6])))
    print("Can partition tabulation: " + str(tabulation_can_partition([1, 1, 3, 4, 7, 3, 5, 18, 19, 23])))
