"""
    Given an array of numbers and a number ‘K’,
    we need to remove ‘K’ numbers from the array such that we are left with maximum distinct numbers.

    Example 1:
    Input: [7, 3, 5, 8, 5, 3, 3], and K=2
    Output: 3
    Explanation: We can remove two occurrences of 3 to be left with 3 distinct numbers [7, 3, 8], we have
    to skip 5 because it is not distinct and occurred twice.
    Another solution could be to remove one instance of '5' and '3' each to be left with three
    distinct numbers [7, 5, 8], in this case, we have to skip 3 because it occurred twice.
                            !
    7   3   5   8   5   3   3

    counter = {7:1,3:3,5:2,8:1} k = 2
    store = [(2,5)(3,3)]
    count = 3

    Example 2:
    Input: [3, 5, 12, 11, 12], and K=3
    Output: 2
    Explanation: We can remove one occurrence of 12, after which all numbers will become distinct. Then
    we can delete any two numbers which will leave us 2 distinct numbers in the result.
            !
    3   5   12  11  12

    counter = {3:1, 5: 1, 12:2, 11:1} k = 3
    result  = [3,5,12,11]
    len(result) - k

    Example 3:
    Input: [1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], and K=2
    Output: 3
    Explanation: We can remove one occurrence of '4' to get three distinct numbers.

    counter = {1:1, 2:1,3:4, 4:2, 5:5}
    min - heap 1, 2, 4,3,5
"""

from collections import Counter
from heapq import heappush, heappop


def find_maximum_distinct_elements(nums, k):
    counter = Counter(nums)
    store = []
    count = 0

    for _, v in counter.items():
        if v > 1:
            heappush(store, v)
        else:
            count += 1

    while store and k > 0:
        top = heappop(store)
        k -= top - 1
        if k >= 0:
            count += 1

    return count - k


if __name__ == '__main__':
    print("Maximum distinct numbers after removing K numbers: " + str(
        find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
    print("Maximum distinct numbers after removing K numbers: " + str(
        find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
    print("Maximum distinct numbers after removing K numbers: " + str(
        find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))
