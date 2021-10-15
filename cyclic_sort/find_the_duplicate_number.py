"""
    Problem Statement

    We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’.
    The array has only one duplicate but it can be repeated multiple times.
    Find that duplicate number without using any extra space.
    You are, however, allowed to modify the input array.

    Example 1:
    Input: [1, 4, 4, 3, 2]
    Output: 4

    Example 2:
    Input: [2, 1, 3, 3, 5, 4]
    Output: 3

    Example 3:
    Input: [2, 4, 1, 4, 4]
    Output: 4
"""


def find_duplicate(nums: [int]) -> int:  # S = O(1) T = O(N)
    i = 0
    while i < len(nums):
        if nums[i] != i + 1:
            if nums[nums[i] - 1] == nums[i]:
                return nums[i]
            temp = nums[i]
            nums[i] = nums[temp - 1]
            nums[temp - 1] = temp
        else:
            i += 1

    return -1


if __name__ == '__main__':
    print(find_duplicate([1, 4, 4, 3, 2]))
    print(find_duplicate([2, 1, 3, 3, 5, 4]))
    print(find_duplicate([2, 4, 1, 4, 4]))
