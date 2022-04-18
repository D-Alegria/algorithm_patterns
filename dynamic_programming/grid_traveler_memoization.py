"""
    Say that you are a traveler on a 2D grid. You begin in the top-left corner
    and your goal is to travel to the bottom-right corner. You may move down or right.

    In how many ways can you travel to the gaol on the grid with dimension m*n.

    Write a function gridTraveler(m,n) that calculates this.
"""


def gridTraveler(m, n, memo={}):  # T = O(2(n+m)) S = O(n+m)
    if (m, n) in memo:
        return memo[(m, n)]
    if not m or not n:
        return 0
    if m == 1 and n == 1:
        return 1
    memo[(m, n)] = gridTraveler(m - 1, n, memo) + gridTraveler(m, n - 1, memo)
    return memo[(m, n)]


"""
    n = no of cols
    m = no of rows
    
    time = O(2^(m+n))
    space = O(m+n)
    
    After memoization
    time = O(m+n)
    space = O(m+n)
"""

if __name__ == '__main__':
    print(gridTraveler(1, 1))
    print(gridTraveler(2, 2))
    print(gridTraveler(3, 2))
    print(gridTraveler(3, 3))
    print(gridTraveler(4, 4))
    print(gridTraveler(10, 10))
    print(gridTraveler(18, 18))
