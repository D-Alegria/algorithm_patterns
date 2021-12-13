"""
    Given a set of distinct numbers, find all of its permutations.

    Permutation is defined as the re-arranging of the elements of the set.
    For example, {1, 2, 3} has the following six permutations:

    {1, 2, 3}
    {1, 3, 2}
    {2, 1, 3}
    {2, 3, 1}
    {3, 1, 2}
    {3, 2, 1}
    If a set has ‘n’ distinct elements it will have n!n! permutations.

    Example 1:
    Input: [1,3,5]
    Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]

    0[]
    1[1]
    3[1,3][3,1]
    5[5,1,3][1,5,3][1,3,5][3,1,5][3,5,1][5,3,1]

    1,3
    [[3,1],[1,3]]
    1 []
    3 [1] 1
"""
from collections import deque


def find_permutations(nums):
    result = []
    permutations = deque()
    # create an empty list as our base case
    permutations.append([])
    # for each num in nums
    for num in nums:  # O(N)
        n = len(permutations)
        # for each perm in permutations
        for _ in range(n):  # O(N)
            # get the current permutation
            # get the len of current permutation
            current = permutations.popleft()
            currentLen = len(current)
            # iterate j through the len
            for i in range(currentLen + 1):  # O(N)
                # insert num at i
                temp = current[:]
                temp.insert(i, num)  # O(N)
                # if len of nums = len of perm add to result
                if len(nums) == len(temp):
                    result.append(temp)
                # else add to permutations
                else:
                    permutations.append(temp)
    return result


if __name__ == '__main__':
    print(find_permutations([1, 3]))
    print(find_permutations([1, 3, 5]))
