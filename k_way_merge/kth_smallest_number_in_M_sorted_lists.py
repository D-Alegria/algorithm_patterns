"""
    Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

    Example 1:
    Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
    Output: 4
    Explanation: The 5th smallest number among all the arrays is 4,
    this can be verified from the merged
    list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]

    Example 2:
    Input: L1=[5, 8, 9], L2=[1, 7], K=3
    Output: 7
    Explanation: The 3rd smallest number among all the arrays is 7.

                           !
    [2, 6, 8], [3, 6, 7], [1, 3, 4]
    count = 4
    i = 0
    [4,6,6]
"""

from heapq import heappush, heappop, heappushpop


def find_k_smallest_number(lists, k):
    minHeap = []

    for idx, li in enumerate(lists):
        heappush(minHeap, (li[0], idx, 0))  # val, r, c

    while k - 1:
        val, r, c = heappop(minHeap)

        if c < len(lists[r]) - 1:
            heappush(minHeap, (lists[r][c + 1], r, c + 1))
        k -= 1

    return heappop(minHeap)[0]


if __name__ == '__main__':
    print("Kth smaller number is: " + str(find_k_smallest_number([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))
    print("Kth smaller number is: " + str(find_k_smallest_number([[5, 8, 9], [1, 7]], 3)))
