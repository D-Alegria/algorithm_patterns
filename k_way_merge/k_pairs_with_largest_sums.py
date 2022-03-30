"""
    K Pairs with Largest Sums (Hard) #
    Given two sorted arrays in descending order,
    find ‘K’ pairs with the largest sum where each pair consists
    of numbers from both the arrays.

    Example 1:
    Input: L1=[9, 8, 2], L2=[6, 3, 1], K=3
    Output: [9, 3], [9, 6], [8, 6]
    Explanation: These 3 pairs have the largest sum. No other pair has a sum larger than any of these.

    Example 2:
    Input: L1=[5, 2, 1], L2=[2, -1], K=3
    Output: [5, 2], [5, -1], [2, 2]
"""

from heapq import heappop, heappush


def find_k_largest_pairs(nums1, nums2, k):
    largest = [-(nums1[0] + nums2[0]), 0, 0]  # sum, nums1 column, nums2 column
    pq = [largest]
    seen = set()
    result = []

    while k - 1:
        top = heappop(pq)
        result.append([nums1[top[1]], nums2[top[2]]])
        k -= 1

        for i in range(2):
            next_ = top[:]
            if i == 0:
                if top[i + 1] >= len(nums1) - 1:
                    continue
                next_[0] += nums1[next_[i + 1]]
                next_[i + 1] += 1
                next_[0] -= nums1[next_[i + 1]]
            else:
                if top[i + 1] >= len(nums2) - 1:
                    continue
                next_[0] += nums2[next_[i + 1]]
                next_[i + 1] += 1
                next_[0] -= nums2[next_[i + 1]]

            if tuple(next_) in seen:
                continue
            seen.add(tuple(next_))
            heappush(pq, next_)
    result.append([nums1[pq[0][1]], nums2[pq[0][2]]])
    return result


if __name__ == '__main__':
    print("Pairs with largest sum are: " + str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3)))
    print("Pairs with largest sum are: " + str(find_k_largest_pairs([5, 2, 1], [2, -1], 3)))
