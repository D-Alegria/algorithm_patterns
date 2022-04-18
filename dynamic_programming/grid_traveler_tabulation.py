def gridTraveler(m, n):
    table = [[0] * (n + 1) for _ in range(m + 1)]
    table[1][1] = 1

    for row in range(m + 1):
        for col in range(n + 1):
            if col < n:
                table[row][col + 1] += table[row][col]
            if row < m:
                table[row + 1][col] += table[row][col]

    return table[m][n]


"""
    n = no of cols
    m = no of rows
    
    time = O(mn)
    space = O(mn)
"""
if __name__ == '__main__':
    print(gridTraveler(2, 2))
    print(gridTraveler(1, 1))
    print(gridTraveler(3, 2))
    print(gridTraveler(3, 3))
    print(gridTraveler(4, 4))
    print(gridTraveler(10, 10))
    print(gridTraveler(18, 18))
