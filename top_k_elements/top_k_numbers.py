"""
    Given an unsorted array of numbers,
    find the ‘K’ largest numbers in it.

    Note: For a detailed discussion about different approaches to solve this problem,
    take a look at Kth Smallest Number.

    Example 1:
    Input: [3, 1, 5, 12, 2, 11], K = 3
    Output: [5, 12, 11]

    Example 2:
    Input: [5, 12, 11, -1, 12], K = 3
    Output: [12, 11, 12]
"""

import heapq


def find_top_k_elements(arr, k):
    minHeap = []

    for i in range(k):
        heapq.heappush(minHeap, arr[i])

    for i in range(k, len(arr)):
        if arr[i] > minHeap[0]:
            heapq.heappop(minHeap)
            heapq.heappush(minHeap, arr[i])
    return list(minHeap)


if __name__ == '__main__':
    print(find_top_k_elements([3, 1, 5, 12, 2, 11], 3))
    print(find_top_k_elements([5, 12, 11, -1, 12], 3))
