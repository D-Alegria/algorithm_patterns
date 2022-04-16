"""
    Write a function howSum(targetSum, numbers) that takes in a targetSum and an
    array of numbers as arguments.

    The function should return an array containing any combination of elements that
    add up to exactly the targetSum. If there is no combination that adds up to the
    targetSum, then return null.

    If there are multiple combinations possible, you may return any single one.
"""


# def howSum(targetSum, numbers):
#     result = []
#
#     def process(targetSum1, currentNums, memo={}):
#         if targetSum1 == 0:
#             result.append(currentNums)
#         if targetSum1 < 0:
#             return
#
#         for num in numbers:
#             remainder = targetSum1 - num
#             temp = currentNums[:]
#             temp.append(num)
#             process(remainder, temp)
#
#     process(targetSum, [])
#     return result


def howSum(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    for num in numbers:
        remainder = targetSum - num
        result = howSum(remainder, numbers, memo)
        if result is not None:
            result.append(num)
            memo[targetSum] = result
            return memo[targetSum]

    memo[targetSum] = None
    return memo[targetSum]


if __name__ == '__main__':
    print(howSum(5, [2, 3]))
    print(howSum(7, [5, 3, 4, 7]))
    print(howSum(7, [2, 4]))
    print(howSum(8, [2, 3, 5]))
    print(howSum(300, [7, 14]))
