def howSum(targetSum, numbers):
    table = [None] * (targetSum + 1)
    table[0] = []

    for i in range(targetSum + 1):
        if table[i] is not None:
            for num in numbers:
                if i + num < targetSum + 1:
                    table[i + num] = [*table[i], num]

    return table[targetSum]


"""
    m = target
    n = len of arr

    time = O(m*n*m)
    space = O(m)
"""

if __name__ == '__main__':
    print(howSum(5, [2, 3]))
    print(howSum(7, [5, 3, 4, 7]))
    print(howSum(7, [2, 4]))
    print(howSum(8, [2, 3, 5]))
    print(howSum(300, [7, 14]))
