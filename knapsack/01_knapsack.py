"""
    Problem Statement #
    Given two integer arrays to represent weights and profits of ‘N’ items,
    we need to find a subset of these items which will give us maximum profit
    such that their cumulative weight is not more than a given number ‘C’.
    Each item can only be selected once, which means either we put an item in the
    knapsack or we skip it.
"""


def knapsack_recursive(dp, profits, weights, capacity, currentIndex):
    if capacity <= 0 or currentIndex >= len(profits):
        return 0

    if dp[currentIndex][capacity] != -1:
        return dp[currentIndex][capacity]

    profit = 0
    if weights[currentIndex] <= capacity:
        profit = profits[currentIndex] + knapsack_recursive(dp, profits, weights, capacity - weights[currentIndex],
                                                            currentIndex + 1)

    profit2 = knapsack_recursive(dp, profits, weights, capacity, currentIndex + 1)

    dp[currentIndex][capacity] = max(profit, profit2)
    return dp[currentIndex][capacity]


def basic_solution(profits, weights, capacity):
    dp = [[-1 for _ in range(capacity + 1)] for _ in range(len(profits))]
    return knapsack_recursive(dp, profits, weights, capacity, 0)


def tabulation_knapsack(profits, weights, capacity):
    table = [[0 for _ in range(capacity + 1)] for _ in range(len(profits))]

    for c in range(capacity + 1):
        if weights[0] <= c:
            table[0][c] = profits[0]

    for i in range(1, len(profits)):
        for c in range(1, capacity + 1):
            profit1 = table[i - 1][c]
            profit2 = 0
            if weights[i] <= c:
                profit2 = profits[i] + table[i - 1][c - weights[i]]

            table[i][c] = max(profit1, profit2)

    return table[-1][-1]


"""
    DFS
    C = capacity
    N = no of items
    
    time = O(2^N)
    space = o(N)
    
    After memoization
    time = O(N*C)
    space = O(N*C)
    
    Tabulation
    time = O(N*C)
    space = O(N*C) 
"""

if __name__ == '__main__':
    print(basic_solution([4, 5, 3, 7], [2, 3, 1, 4], 5))
    print(basic_solution([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(basic_solution([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(basic_solution([1, 6, 10, 16], [1, 2, 3, 5], 8))
    print(tabulation_knapsack([4, 5, 3, 7], [2, 3, 1, 4], 5))
    print(tabulation_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(tabulation_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(tabulation_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 8))
