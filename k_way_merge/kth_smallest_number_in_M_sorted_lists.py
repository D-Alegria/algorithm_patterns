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
    i = 1
    [4,3,3,2,1]
"""

from heapq import heappush, heappop, heappushpop


def find_k_smallest_number(lists, k):
    maxHeap = []

    lists.sort(key=lambda x: x[0])
    print(lists)

    count = 0
    i = 0
    maxlength = 0

    for li in lists:
        maxlength = max(maxlength, len(li))

    while i < maxlength:
        for li in lists:
            if i < len(li):
                if count < k:
                    heappush(maxHeap, -li[i])
                else:
                    if -maxHeap[0] > li[i]:
                        heappushpop(maxHeap, -li[i])
                count += 1
        i += 1

    return -heappop(maxHeap)


if __name__ == '__main__':
    print("Kth smaller number is: " + str(find_k_smallest_number([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))
    print("Kth smaller number is: " + str(find_k_smallest_number([[5, 8, 9], [1, 7]], 3)))
