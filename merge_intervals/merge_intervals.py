"""
    Problem Statement #
    Given a list of intervals,
    merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

    Example 1:
    Intervals: [[1,4], [2,5], [7,9]]
    Output: [[1,5], [7,9]]
    Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into
    one [1,5].

    1   2   3   4   5   6   7   8   9
    !           !
        !           !
                            !       !

    Example 2:
    Intervals: [[6,7], [2,4], [5,9]]
    Output: [[2,4], [5,9]]
    Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].

    2   3   4   5   6   7   8   9
    !       !
                !               !
                    !   !

    Example 3:
    Intervals: [[1,4], [2,6], [3,5]]
    Output: [[1,6]]
    Explanation: Since all the given intervals overlap, we merged them into one.

    1   2   3   4   5   6
    !           !
        !               !
            !       !
"""


def merge_intervals(arr: [[int]]) -> [[int]]:
    fast, slow = 1, 0
    arr.sort(key=lambda a: a[0])
    result = [arr[0]]

    while fast < len(arr):
        current = result[slow]
        if current[1] >= arr[fast][0]:
            result[slow] = [current[0], max(current[1], arr[fast][1])]
        else:
            result.append([arr[fast][0], arr[fast][1]])
            slow += 1
        fast += 1

    return result


def merge_intervals_1(arr: [[int]]) -> [[int]]:
    arr.sort(key=lambda a: a[0])
    result = [arr[0]]

    for i in range(1, len(arr)):
        last = len(result) - 1
        if arr[i][0] < result[last][1]:
            result[last] = [result[last][0], max(arr[i][1], result[last][1])]
        else:
            result.append(arr[i])

    return result


if __name__ == '__main__':
    print(merge_intervals([[1, 4], [2, 5], [7, 9]]))  # [[1,5], [7,9]]
    print(merge_intervals([[6, 7], [2, 4], [5, 9]]))  # [[2,4], [5,9]]
    print(merge_intervals([[1, 4], [2, 6], [3, 5]]))  # [[1,6]]
