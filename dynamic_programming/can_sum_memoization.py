"""
    Write a function canSum(targetSum, numbers) that takes in a targetSum and
    an array of number has arguments.

    The function should return a boolean indicating whether it is possible
    to generate the targetSum using numbers from the array.

    You may use an element of the array as many times as needed.

    You may assume that all input numbers are non-negative.
"""


def canSum(n, arr, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return True
    if n < 0:
        return False

    for i in arr:
        reminder = n - i
        if canSum(reminder, arr, memo):
            return True

    memo[n] = False
    return False


if __name__ == '__main__':
    print(canSum(7, [5, 3, 4, 7]))
    print(canSum(5, [2, 3]))
    print(canSum(7, [2, 4]))
    print(canSum(300, [7, 14]))
