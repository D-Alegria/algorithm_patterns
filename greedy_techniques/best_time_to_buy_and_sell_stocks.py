from typing import List


def maxProfit(prices: List[int]) -> int:
    buyDay = 0
    max_profit = 0

    for sellDay in range(1, len(prices)):
        max_profit = max(max_profit, prices[sellDay] - prices[buyDay])
        if prices[buyDay] > prices[sellDay]:
            buyDay = sellDay

    return max_profit


if __name__ == '__main__':
    print(maxProfit([7, 1, 5, 3, 6, 4]))
    print(maxProfit([7, 6, 4, 3, 1]))
    print(maxProfit([2, 1, 4]))
    print(maxProfit([2, 4, 1]))
