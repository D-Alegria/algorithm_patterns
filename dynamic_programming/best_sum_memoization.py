"""
    Write a function bestSum(targetSum, numbers) that takes in a targetSum and
    an array of numbers as arguments.

    The function should return an array containing the shortest combination of
    numbers that add up to exactly the targetSum.

    If there is a tie for the shortest combination, you may return any one of the
    shortest.
"""


def bestSum(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    miniSum = None
    for num in numbers:
        remainder = targetSum - num
        result = bestSum(remainder, numbers, memo)

        if result is not None:
            combination = [*result, num]
            if not miniSum or len(combination) < len(miniSum):
                miniSum = combination

    memo[targetSum] = miniSum
    return memo[targetSum]


"""
    n = number of items in the list
    m = targetSum

    time: O(n^m*m)
    space: O(m*m)
    
    After memoization
    time: O(n*m*m)
    space: O(m*m*m)
"""

if __name__ == '__main__':
    print(bestSum(7, [5, 3, 4, 7]))
    print(bestSum(8, [2, 3, 5]))
    print(bestSum(8, [1, 4, 5]))
    print(bestSum(100, [1, 2, 5, 25]))
