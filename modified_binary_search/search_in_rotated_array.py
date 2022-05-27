"""
    Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number,
    find if a given ‘key’ is present in it.

    Write a function to return the index of the ‘key’ in the rotated array. If the ‘key’ is not present,
    return -1. You can assume that the given array does not have any duplicates.

    Example 1:
    Input: [10, 15, 1, 3, 8], key = 15
    Output: 1
    Explanation: '15' is present in the array at index '1'.

    !
    10, 15, 1, 3, 8
                  ^
    Example 2:
    Input: [4, 5, 7, 9, 10, -1, 2], key = 10
    Output: 4
    Explanation: '10' is present in the array at index '4'.


    Formula: If a sorted array is shifted, if you take the middle, always one side will be sorted.
    Take the recursion according to that rule.

    1- take the middle and compare with target, if matches return.
    2- if middle is bigger than left side, it means left is sorted
    2a- if [left] < target < [middle] then do recursion with left, middle - 1 (right)
    2b- left side is sorted, but target not in here, search on right side middle + 1 (left), right
    3- if middle is less than right side, it means right is sorted
    3a- if [middle] < target < [right] then do recursion with middle + 1 (left), right
    3b- right side is sorted, but target not in here, search on left side left, middle -1 (right)
"""


def search_rotated_array(arr, key):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == key:
            return mid
        elif arr[start] <= arr[mid]:
            if arr[start] <= key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if arr[mid] < key <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1


if __name__ == '__main__':
    print(search_rotated_array([10, 15, 1, 3, 8], 15))
    print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))
    print(search_rotated_array([4, 5, 6, 7, 0, 1, 2], 0))
