"""
    Problem Statement #
    Given a list of non-overlapping intervals sorted by their start time,
    insert a given interval at the correct position and merge all
    necessary intervals to produce a list that has only mutually exclusive intervals.

    Example 1:
    Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
    Output: [[1,3], [4,7], [8,12]]
    Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

    1   2   3   4   5   6   7   8   9   10  11  12
    !       !
                !       !
                    !       !
                                !                 !
    Example 2:
    Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
    Output: [[1,3], [4,12]]
    Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].

    Example 3:
    Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
    Output: [[1,4], [5,7]]
    Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].
"""


def insert_interval(intervals: [[int]], new_interval: [[int]]) -> [[int]]:
    intervals.append(new_interval)
    intervals.sort(key=lambda a: a[0])
    result = [intervals[0]]

    for i in range(1, len(intervals)):
        current = result[-1]
        if current[1] >= intervals[i][0]:
            result[-1][1] = max(current[1], intervals[i][1])
        else:
            result.append([intervals[i][0], intervals[i][1]])

    return result


if __name__ == '__main__':
    print(insert_interval([[1, 3], [5, 7], [8, 12]], [4, 6]))  # [[1,3], [4,7], [8,12]]
    print(insert_interval([[1, 3], [5, 7], [8, 12]], [4, 10]))  # [[1,3], [4,12]]
    print(insert_interval([[2, 3], [5, 7]], [1, 4]))  # [[1,4], [5,7]]
