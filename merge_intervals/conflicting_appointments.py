"""
    Given an array of intervals representing ‘N’ appointments,
    find out if a person can attend all the appointments.

    Example 1:
    Appointments: [[1,4], [2,5], [7,9]]
    Output: false
    Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.

    Example 2:
    Appointments: [[6,7], [2,4], [8,12]]
    Output: true
    Explanation: None of the appointments overlap, therefore a person can attend all of them.

    Example 3:
    Appointments: [[4,5], [2,3], [3,6]]
    Output: false
    Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.
"""


def can_attend_all_appointments(intervals: [[int]]) -> bool:  # S = O(1); T = O(N)
    intervals.sort(key=lambda a: a[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] <= intervals[i - 1][1]:
            return False
    return True


if __name__ == '__main__':
    print(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]]))  # False
    print(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]]))  # True
    print(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]]))  # False
