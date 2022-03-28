"""
    Problem Statement #
    Given an N * N matrix where each row and column is sorted in ascending order,
     find the Kth smallest element in the matrix.

    Example 1:

    Input: Matrix=[
        [2, 6, 8],
        [3, 7, 10],
        [5, 8, 11]
      ],
      K=5
    Output: 7
    Explanation: The 5th smallest number in the matrix is 7.
"""

from heapq import heappush, heappop


def find_k_smallest_number(matrix, k):
    minHeap = []

    for idx, li in enumerate(matrix):
        heappush(minHeap, (li[0], idx, 0))

    while k - 1:
        val, r, c = heappop(minHeap)

        if c < len(matrix[r]) - 1:
            heappush(minHeap, (matrix[r][c + 1], r, c + 1))
        k -= 1
    return heappop(minHeap)[0]


if __name__ == '__main__':
    print("Kth smallest number is: " + str(find_k_smallest_number([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))
    print("Kth smallest number is: " + str(find_k_smallest_number([[5, 8, 9], [1, 7]], 3)))
    print("Kth smallest number is: " + str(find_k_smallest_number([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))
