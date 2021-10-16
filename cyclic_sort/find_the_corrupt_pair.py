"""
    Find the Corrupt Pair (easy)

    We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’.
    The array originally contained all the numbers from 1 to ‘n’, but due to a data error,
    one of the numbers got duplicated which also resulted in one number going missing.
    Find both these numbers.

    Example 1:
    Input: [3, 1, 2, 5, 2]
    Output: [2, 4]
    Explanation: '2' is duplicated and '4' is missing.

    Example 2:
    Input: [3, 1, 2, 3, 6, 4]
    Output: [3, 5]
    Explanation: '3' is duplicated and '5' is missing.
"""


def find_corrupt_numbers(nums: [int]) -> [int]:  # T = O(N), S = O(1)
    i = 0
    while i < len(nums):  # O(N)
        if nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
            temp = nums[i]
            nums[i] = nums[temp - 1]
            nums[temp - 1] = temp
        else:
            i += 1

    for i, n in enumerate(nums):  # O(N)
        if i != n - 1:
            return [nums[i], i + 1]
    return []


if __name__ == '__main__':
    print(find_corrupt_numbers([3, 1, 2, 5, 2]))
    print(find_corrupt_numbers([3, 1, 2, 3, 6, 4]))
