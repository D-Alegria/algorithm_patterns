"""
    Minimum Meeting Rooms (hard) #
    Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms required to hold all the meetings.

    Example 1:
    Meetings: [[1,4], [2,5], [7,9]]
    Output: 2
    Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these two meetings. [7,9] can
    occur in any of the two rooms later.

    Example 2:
    Meetings: [[6,7], [2,4], [8,12]]
    Output: 1
    Explanation: None of the meetings overlap, therefore we only need one room to hold all meetings.

    Example 3:
    Meetings: [[1,4], [2,3], [3,6]]
    Output:2
    Explanation: Since [1,4] overlaps with the other two meetings [2,3] and [3,6], we need two rooms to
    hold all the meetings.

    Example 4:
    Meetings: [[4,5], [2,3], [2,4], [3,5]]
    Output: 2
    Explanation: We will need one room for [2,3] and [3,5], and another room for [2,4] and [4,5].
"""


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def min_meeting_rooms(meetings: [Meeting]) -> int:  # T=O(N^2) S=O(N)
    meetings.sort(key=lambda m: m.start)  # O(N Log N)
    rooms = [meetings[0].end]

    for i in range(1, len(meetings)):  # O(N)
        temp_rooms = rooms.copy()
        update = False
        for j in range(len(temp_rooms)):  # O(N)
            if meetings[i].start >= temp_rooms[j]:
                rooms[j] = meetings[i].end
                update = True
            if update:
                break
        if not update:
            rooms.append(meetings[i].end)

    return len(rooms)


if __name__ == '__main__':
    print(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)]))  # 2
    print(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)]))  # 1
    print(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)]))  # 2
    print(min_meeting_rooms([Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)]))  # 2
