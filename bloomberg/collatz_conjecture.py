"""
    The Collatz Conjecture says if you take a positive integer N and
    repeatedly set either N=N/2 (if it's even) or N=3N+1 (if it's odd), N will eventually be 1.
    5 -> 16 -> 8 -> 4 -> 2 -> 1 (5 steps).

    Given N, how many steps does it take to reach 1?
"""


def collatz(n):
    steps = 0
    memo = {}

    while n > 1:
        temp = n
        if n in memo:
            n = memo[n]
            continue
        if n % 2 == 0:
            n /= 2
        else:
            n = (3 * n) + 1
        steps += 1
        memo[temp] = n
    return steps


def collatz_recursive(n, memo=None):
    if memo is None:
        memo = {1: 0}
    if n in memo:
        if n == 1:
            return 0
        return 1 + collatz_recursive(memo[n], memo)
    temp = n
    if n % 2 == 0:
        n /= 2
    else:
        n = (3 * n) + 1
    memo[temp] = n
    return 1 + collatz_recursive(n, memo)


if __name__ == '__main__':
    print(collatz(5))
    print(collatz_recursive(5))
    print(collatz(15))
    print(collatz_recursive(15))
    print(collatz(27))
    print(collatz_recursive(27))
