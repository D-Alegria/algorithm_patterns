"""
    Given ‘N’ ropes with different lengths,
    we need to connect these ropes into one big rope with minimum cost.
    The cost of connecting two ropes is equal to the sum of their lengths.

    Example 1:
    Input: [1, 3, 11, 5]
    Output: 33
    Explanation: First connect 1+3(=4), then 4+5(=9), and then 9+11(=20). So the total cost is 33 (4+9+20)

    Example 2:
    Input: [3, 4, 5, 6]
    Output: 36
    Explanation: First connect 3+4(=7), then 5+6(=11), 7+11(=18). Total cost is 36 (7+11+18)

    Example 3:
    Input: [1, 3, 11, 5, 2]
    Output: 42
    Explanation: First connect 1+2(=3), then 3+3(=6), 6+5(=11), 11+11(=22). Total cost is 42 (3+6+11+22)
"""

import heapq


def connect_ropes(arr):
    min_heap = []
    for i in arr:
        heapq.heappush(min_heap, i)

    result, temp = 0, 0
    while len(min_heap) > 1:
        temp = heapq.heappop(min_heap) + heapq.heappop(min_heap)
        result += temp
        heapq.heappush(min_heap, temp)
    return result


if __name__ == '__main__':
    print(connect_ropes([1, 3, 11, 5]))
    print(connect_ropes([3, 4, 5, 6]))
    print(connect_ropes([1, 3, 11, 5, 2]))
