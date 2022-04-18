def fib(n):
    table = [0] * (n + 1)
    table[1] = 1

    for i in range(n - 1):
        table[i + 1] += table[i]
        table[i + 2] += table[i]

    table[n] += table[n - 1]
    return table[n]


"""
    n = target
    
    time = 0(n)
    space = 0(n)
"""

if __name__ == '__main__':
    print(fib(6))
    print(fib(7))
    print(fib(8))
    print(fib(50))
