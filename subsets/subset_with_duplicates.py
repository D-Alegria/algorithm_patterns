"""
    Problem Statement #
    Given a set of numbers that might contain duplicates, find all of its distinct subsets.

    Example 1:
    Input: [1, 3, 3]
    Output: [], [1], [3], [1,3], [3,3], [1,3,3]

    Example 2:
    Input: [1, 5, 3, 3]
    Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3]

    0[]
    1[][1]
    2[][1][3][1,3]
    3[][1][3][1,3],[3,3][1,3,3]
"""


def find_subSets(nums):
    subsets = [[]]

    nums.sort()

    for i in range(len(nums)):
        start, end = 0, len(subsets)
        if i > 0 and nums[i] == nums[i - 1]:
            start = len(subsets) // 2
        for x in range(start, end):
            current = list(subsets[x])
            current.append(nums[i])
            subsets.append(current)

    return subsets


if __name__ == '__main__':
    print(find_subSets([1, 3, 3]))
    print(find_subSets([1, 5, 3, 3]))
    print(find_subSets([1, 5, 3, 3, 5]))
