"""
    Find the Smallest Missing Positive Number (medium)
    Given an unsorted array containing numbers,
    find the smallest missing positive number in it.

    Example 1:
    Input: [-3, 1, 5, 4, 2]
    Output: 3
    Explanation: The smallest missing positive number is '3'

    Example 2:
    Input: [3, -2, 0, 1, 2]
    Output: 4

    Example 3:
    Input: [3, 2, 5, 1]
    Output: 4
"""


def find_first_missing_positive(nums: [int]) -> int:  # T = O(N) S = O(1)
    i = 0
    while i < len(nums):
        if 0 < nums[i] <= len(nums) and nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
            temp = nums[i]
            nums[i] = nums[temp - 1]
            nums[temp - 1] = temp
        else:
            i += 1

    for i, n in enumerate(nums):
        if n != i + 1:
            return i + 1


if __name__ == '__main__':
    print(find_first_missing_positive([-3, 1, 5, 4, 2]))
    print(find_first_missing_positive([3, -2, 0, 1, 2]))
    print(find_first_missing_positive([3, 2, 5, 1]))
