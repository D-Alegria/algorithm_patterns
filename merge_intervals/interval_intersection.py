"""
    Problem Statement #
    Given two lists of intervals,
    find the intersection of these two lists.
    Each list consists of disjoint intervals sorted on their start time.

    Example 1:
    Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
    Output: [2, 3], [5, 6], [7, 7]
    Explanation: The output list contains the common intervals between the two lists.

    1   2   3   4   5   6   7   8   9
        *   *
    !       !
                    *       *
                    !   !
                            !       !

    Example 2:
    Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
    Output: [5, 7], [9, 10]
    Explanation: The output list contains the common intervals between the two lists.

    1   2   3   4   5   6   7   8   9   10  11  12
                    *                   *
                    !       !
                                    !   !
"""


def intersect(arr1: [[int]], arr2: [[int]]) -> [[int]]:  # S = O(N) T = O(N) N is the longest array
    result = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr2[j][0] <= arr1[i][1]:
            result.append([max(arr1[i][0], arr2[j][0]), min(arr1[i][1], arr2[j][1])])
        if arr2[j][1] > arr1[i][1]:
            i += 1
        else:
            j += 1

    return result


if __name__ == '__main__':
    print(intersect([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]]))  # [2, 3], [5, 6], [7, 7]
    print(intersect([[1, 3], [5, 7], [9, 12]], [[5, 10]]))  # [5, 7], [9, 10]
