"""
    Find the First K Missing Positive Numbers (hard)

    Given an unsorted array containing numbers and a number ‘k’,
    find the first ‘k’ missing positive numbers in the array.

    Example 1:
    Input: [3, -1, 4, 5, 5], k=3
    Output: [1, 2, 6]
    Explanation: The smallest missing positive numbers are 1, 2 and 6.

    Example 2:
    Input: [2, 3, 4], k=3
    Output: [1, 5, 6]
    Explanation: The smallest missing positive numbers are 1, 5 and 6.

    Example 3:
    Input: [-2, -3, 4], k=2
    Output: [1, 2]
    Explanation: The smallest missing positive numbers are 1 and 2.
"""


def find_first_k_missing_positive(nums: [int], k: int) -> [int]:  # S = O(N) T = O(N)
    i = 0
    maxi = 0
    while i < len(nums):
        maxi = max(maxi, nums[i])
        if 0 < nums[i] <= len(nums) and nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
            temp = nums[i]
            nums[i] = nums[temp - 1]
            nums[temp - 1] = temp
        else:
            i += 1
    print(nums)
    result = []
    for i, n in enumerate(nums):
        if i != n - 1:
            result.append(i + 1)

        if len(result) == k:
            return result
    j = 1
    while len(result) != k:
        result.append(maxi + j)
        j += 1

    return result


if __name__ == '__main__':
    print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
    print(find_first_k_missing_positive([2, 3, 4], 3))
    print(find_first_k_missing_positive([-2, -3, 4], 2))
