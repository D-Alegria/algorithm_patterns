"""
    Problem Statement #
    Given ‘M’ sorted arrays, find the smallest range that
    includes at least one number from each of the ‘M’ lists.

    Example 1:

    Input: L1=[1, 5, 8], L2=[4, 12], L3=[7, 8, 10]
    Output: [4, 7]
    Explanation: The range [4, 7] includes 5 from L1, 4 from L2 and 7 from L3.
    Example 2:

    Input: L1=[1, 9], L2=[4, 12], L3=[7, 10, 16]
    Output: [9, 12]
    Explanation: The range [9, 12] includes 9 from L1, 12 from L2 and 10 from L3.

    [1]
"""
import math
from heapq import heappush, heappop


def find_smallest_range(lists):
    minHeap = []
    rangeStart, rangeEnd = 0, math.inf
    currentMaxNumber = -math.inf

    for idx, arr in enumerate(lists):
        heappush(minHeap, (arr[0], idx, 0))
        currentMaxNumber = max(currentMaxNumber, arr[0])

    while len(minHeap) == len(lists):
        val, r, c = heappop(minHeap)

        if rangeEnd - rangeStart > currentMaxNumber - val:
            rangeStart, rangeEnd = val, currentMaxNumber

        if c < len(lists[r]) - 1:
            heappush(minHeap, (lists[r][c + 1], r, c + 1))
            currentMaxNumber = max(currentMaxNumber, lists[r][c + 1])
    return [rangeStart, rangeEnd]


if __name__ == '__main__':
    print("Smallest range is: " + str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))
    print("Smallest range is: " + str(find_smallest_range([[1, 9], [4, 12], [7, 10, 16]])))
