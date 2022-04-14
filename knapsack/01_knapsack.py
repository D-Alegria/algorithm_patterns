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


if __name__ == '__main__':
    print(basic_solution([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(basic_solution([1, 6, 10, 16], [1, 2, 3, 5], 7))
