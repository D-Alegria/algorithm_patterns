"""
    Given a set with distinct elements, find all of its distinct subsets.

    Example 1:
    Input: [1, 3]
    Output: [], [1], [3], [1,3]

    Example 2:
    Input: [1, 5, 3]
    Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]

    start with an empty array

    iterate through the array

    add the current value into all the values in the current array

"""


def findSubSets(nums):
    subsets = [[]]

    for i in nums:
        n = len(subsets)
        for x in range(n):
            current = list(subsets[x])
            current.append(i)
            subsets.append(current)

    return subsets


if __name__ == '__main__':
    print(findSubSets([1, 3]))
    print(findSubSets([1, 3, 5]))
