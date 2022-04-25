def bestSum(targetSum, numbers):
    table = [None] * (targetSum + 1)
    table[0] = []

    for i in range(targetSum + 1):
        if table[i] is not None:
            for num in numbers:
                if i + num < targetSum + 1:
                    if not table[i + num] or len(table[i]) + 1 < len(table[i + num]):
                        table[i + num] = [*table[i], num]
    return table[targetSum]


"""
    n = number of items in the list
    m = targetSum
    
    time: O(n*m*m)
    space: O(m*m)
"""
if __name__ == '__main__':
    print(bestSum(7, [5, 3, 4, 7]))
    print(bestSum(8, [2, 3, 5]))
    print(bestSum(8, [1, 4, 5]))
    print(bestSum(100, [1, 2, 5, 25]))
