"""
    Write a function fib(n) that takes in a number as an argument.
    The function should return the n-th number of the Fibonacci sequence.

    fib(1) = 1
    fib(2) = fib(1) + fib(0) = 1 + 0 = 1
    fib(3) = fib(2) + fib(1) = 1 + 1 = 2
    fib(4) = fib(3) + fib(2) = 2 + 1 = 3
"""


def fib(n, memo={}):  # S = O(n) T = O(n)
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


if __name__ == '__main__':
    print(fib(5))
    print(fib(7))
    print(fib(50))
