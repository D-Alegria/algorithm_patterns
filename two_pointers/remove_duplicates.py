"""
    Problem Statement #
    Given an array of sorted numbers, remove all duplicates from it.
    You should not use any extra space;
    after removing the duplicates in-place return the new length of the array.

    Example 1:
    Input: [2, 3, 3, 3, 6, 9, 9]
    Output: 4
    Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

    Example 2:
    Input: [2, 2, 2, 11]
    Output: 2
    Explanation: The first two elements after removing the duplicates will be [2, 11].
"""
from typing import List


def remove_duplicates(arr: List[int]) -> int:
    front = 1
    back = 0
    count = 1

    for i in range(len(arr) - 1):
        if arr[front] != arr[back]:
            count += 1
            back = front
        front += 1

    return count


if __name__ == '__main__':
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))  # 4
    print(remove_duplicates([2, 2, 2, 11]))  # 2
