"""
    Problem Statement #
    We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’.
    The array has some duplicates, find all the duplicate numbers without using any extra space.

    Example 1:
    Input: [3, 4, 4, 5, 5]
    Output: [4, 5]

    Example 2:
    Input: [5, 4, 7, 2, 3, 5, 3]
    Output: [3, 5]
"""


def find_all_duplicates(nums: [int]) -> [int]:  # S = O(1) T = O(N)
    i = 0
    result = set()
    while i < len(nums):
        if nums[i] != i + 1:
            if nums[nums[i] - 1] == nums[i]:
                result.add(nums[i])
                i += 1
                continue
            temp = nums[i]
            nums[i] = nums[temp - 1]
            nums[temp - 1] = temp
        else:
            i += 1

    return list(result)


if __name__ == '__main__':
    print(find_all_duplicates([1, 4, 4, 3, 2]))
    print(find_all_duplicates([2, 1, 3, 3, 5, 4]))
    print(find_all_duplicates([2, 4, 1, 4, 4]))
    print(find_all_duplicates([3, 4, 4, 5, 5]))
    print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))
