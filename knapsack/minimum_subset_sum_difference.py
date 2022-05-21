"""
    Problem Statement#
    Given a set of positive numbers,
    partition the set into two subsets with minimum difference between their subset sums.

    Example 1:
    Input: {1, 2, 3, 9}
    Output: 3
    Explanation: We can partition the given set into two subsets where minimum absolute difference
    between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.

    Example 2:
    Input: {1, 2, 7, 1, 5}
    Output: 0
    Explanation: We can partition the given set into two subsets where minimum absolute difference
    between the sum of number is '0'. Following are the two subsets: {1, 2, 5} & {7, 1}.

    Example 3:
    Input: {1, 3, 100, 4}
    Output: 92
    Explanation: We can partition the given set into two subsets where minimum absolute difference
    between the sum of numbers is '92'. Here are the two subsets: {1, 3, 4} & {100}.
"""


def tabulation_can_partition(nums):
    total = sum(nums)
    n = len(nums)
    table = [[False for __ in range((total // 2) + 1)] for _ in range(n)]

    for i in range(n):
        table[i][0] = True

    table[0][nums[0]] = True

    for i in range(1, n):
        for t in range(1, (total // 2) + 1):
            withNum = False
            if nums[i] <= t:
                withNum = table[i - 1][t - nums[i]]
            withOutNum = table[i - 1][t]

            table[i][t] = withNum or withOutNum

    sum1 = 0
    for i in range(total // 2, -1, -1):
        if table[n - 1][i]:
            sum1 = i
            break

    sum2 = total - sum1
    return abs(sum2 - sum1)


def memoization_can_partition(nums):
    total = sum(nums)
    memo = [[-1 for __ in range(total + 1)] for _ in range(len(nums))]
    return find_difference(nums, 0, 0, 0, memo)


def find_difference(nums, currentIndex, sum1, sum2, memo):
    if currentIndex >= len(nums):
        return abs(sum1 - sum2)

    if memo[currentIndex][sum1] > -1:
        return memo[currentIndex][sum1]

    if memo[currentIndex][sum2] > -1:
        return memo[currentIndex][sum2]

    diff_1 = find_difference(nums, currentIndex + 1, sum1, sum2 + nums[currentIndex], memo)
    diff_2 = find_difference(nums, currentIndex + 1, sum1 + nums[currentIndex], sum2, memo)
    # print(f"i: {currentIndex}, d1:{diff_1}, d2: {diff_2}")

    memo[currentIndex][sum1] = min(diff_1, diff_2)
    return memo[currentIndex][sum1]


"""
    DFS
    S = Total sum of items
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
    print("Can partition memoization: " + str(memoization_can_partition([1, 2, 3, 9])))
    print("Can partition memoization: " + str(memoization_can_partition([1, 2, 7, 1, 5])))
    print("Can partition memoization: " + str(memoization_can_partition([1, 3, 100, 4])))
    print("Can partition tabulation: " + str(tabulation_can_partition([1, 2, 3, 9])))
    print("Can partition tabulation: " + str(tabulation_can_partition([1, 2, 7, 1, 5])))
    print("Can partition tabulation: " + str(tabulation_can_partition([1, 3, 100, 4])))
