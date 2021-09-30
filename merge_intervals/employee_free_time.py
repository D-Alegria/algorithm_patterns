"""
    Employee Free Time (hard) #
    For ‘K’ employees, we are given a list of intervals representing the working hours of each employee.
    Our goal is to find out if there is a free interval that is common to all employees.
    You can assume that each list of employee working hours is sorted on the start time.

    Example 1:
    Input: Employee Working Hours=[[[1,3], [5,6]], [[2,3], [6,8]]]
    Output: [3,5]
    Explanation: Both the employees are free between [3,5].

    Example 2:
    Input: Employee Working Hours=[[[1,3], [9,12]], [[2,4]], [[6,8]]]
    Output: [4,6], [8,9]
    Explanation: All employees are free between [4,6] and [8,9].

    Example 3:
    Input: Employee Working Hours=[[[1,3]], [[2,4]], [[3,5], [7,9]]]
    Output: [5,7]
    Explanation: All employees are free between [5,7].
"""


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='-')


def printList(schedule: [Interval]):
    for i in schedule:
        i.print_interval()
    print()


def find_employee_free_time(schedule: [[Interval]]) -> [Interval]:  # S=O(N^2) T=o(n log n)
    # merge intervals
    merge_schedules = []
    for i in schedule:  # O(N)
        merge_schedules += i

    merge_schedules.sort(key=lambda x: x.start)  # O(N Log N)
    result = [merge_schedules[0]]

    for i in range(1, len(merge_schedules)):  # O(N)
        current = result[-1]
        if merge_schedules[i].start <= current.end:
            result[-1] = Interval(min(current.start, merge_schedules[i].start),
                                  max(merge_schedules[i].end, current.end))
        else:
            result.append(merge_schedules[i])

    # find gaps between them
    free_time = []
    for i in range(1, len(result)):  # O(K)
        free_time.append(Interval(result[i - 1].end, result[i].start))
    return free_time


if __name__ == '__main__':
    printList(find_employee_free_time([[Interval(1, 3), Interval(5, 6)], [Interval(2, 3), Interval(6, 8)]]))
    printList(find_employee_free_time([[Interval(1, 3), Interval(9, 12)], [Interval(2, 4)], [Interval(6, 8)]]))
    printList(find_employee_free_time([[Interval(1, 3), Interval(2, 4)], [Interval(3, 5), Interval(7, 8)]]))
