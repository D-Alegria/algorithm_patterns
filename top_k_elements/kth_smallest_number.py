"""
    Given an unsorted array of numbers, find Kth smallest number in it.

    Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.

    Note: For a detailed discussion about different approaches to solve this problem,
    take a look at Kth Smallest Number.

    Example 1:
    Input: [1, 5, 12, 2, 11, 5], K = 3
    Output: 5
    Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].

    Example 2:
    Input: [1, 5, 12, 2, 11, 5], K = 4
    Output: 5
    Explanation: The 4th smallest number is '5', as the first three small numbers are [1, 2, 5].

    Example 3:
    Input: [5, 12, 11, -1, 12], K = 3
    Output: 11
    Explanation: The 3rd smallest number is '11', as the first two small numbers are [5, -1].
"""

import heapq


def find_kth_smallest_number_1(nums, k):  # T = O(NLogN), S = O(N)
    minHeap = []
    for i in range(k):
        heapq.heappush(minHeap, -nums[i])

    for i in range(k, len(nums)):
        if - nums[i] > minHeap[0]:
            heapq.heappop(minHeap)
            heapq.heappush(minHeap, -nums[i])

    return minHeap[0] * -1


def find_kth_smallest_number(arr, k):
    heapq.heapify(arr)
    return arr[k - 1]


if __name__ == '__main__':
    print(find_kth_smallest_number([1, 5, 12, 2, 11, 5], 3))
    print(find_kth_smallest_number([1, 5, 12, 2, 11, 5], 4))
    print(find_kth_smallest_number([5, 12, 11, -1, 12], 3))
