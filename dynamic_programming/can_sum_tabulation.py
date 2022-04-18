def canSum(n, arr):
    table = [False] * (n + 1)
    table[0] = True

    for i in range(n + 1):
        for a in arr:
            if i + a < n + 1:
                table[i + a] = table[i] or table[i + a]
    return table[n]


"""
    m = target
    n = len of arr
    
    time = O(mn)
    space = O(m)
"""

if __name__ == '__main__':
    print(canSum(7, [5, 3, 4, 7]))
    print(canSum(5, [2, 3]))
    print(canSum(7, [2, 4]))
    print(canSum(300, [7, 14]))
