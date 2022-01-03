"""
    Given an array of numbers which is sorted in ascending order and is rotated ‘k’ times around a pivot, find ‘k’.

    You can assume that the array does not have any duplicates.

    Example 1:
    Input: [10, 15, 1, 3, 8]
    Output: 2
    Explanation: The array has been rotated 2 times.
        !   *
    10  15  1   3   8
            ^
    start < mid
        start = mid

    start > mid
        end = mid

    Example 2:
    Input: [4, 5, 7, 9, 10, -1, 2]
    Output: 5
    Explanation: The array has been rotated 5 times.
                    !   *
    4   5   7   9   10  -1  2
                        ^


    Example 3:
    Input: [1, 3, 8, 10]
    Output: 0
    Explanation: The array has been not been rotated.
            !   *
    1   3   8   10
                ^
"""


def count_rotations(arr):
    start, end = 0, len(arr) - 1

    if arr[start] < arr[end]:
        return start

    while start < end - 1:
        mid = start + (end - start) // 2

        if arr[start] == arr[mid] and arr[mid] == arr[end]:
            start += 1

        if arr[start] <= arr[mid]:
            start = mid
        else:
            end = mid

    return end


if __name__ == '__main__':
    print(count_rotations([10, 15, 1, 3, 8]))
    print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
    print(count_rotations([1, 3, 8, 10]))
    print(count_rotations([3, 3, 7, 3]))
