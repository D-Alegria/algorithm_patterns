"""
    Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number,
    find if a given ‘key’ is present in it.

    Write a function to return the index of the ‘key’ in the rotated array. If the ‘key’ is not present,
    return -1. You can assume that the given array does not have any duplicates.

    Example 1:
    Input: [10, 15, 1, 3, 8], key = 15
    Output: 1
    Explanation: '15' is present in the array at index '1'.

    Example 2:
    Input: [4, 5, 7, 9, 10, -1, 2], key = 10
    Output: 4
    Explanation: '10' is present in the array at index '4'.
"""


def search_rotated_array(arr, key):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[start] == arr[mid] and arr[end] == arr[mid]:
            start += 1
            end -= 1

        if arr[start] <= arr[mid]:
            if key > arr[mid]:
                start = mid + 1
            elif key < arr[mid]:
                end = mid - 1
            else:
                return mid
        else:
            if key > arr[mid]:
                end = mid - 1
            elif key < arr[mid]:
                start = mid + 1
            else:
                return mid
    return -1


if __name__ == '__main__':
    print(search_rotated_array([3, 7, 3, 3, 3], 7))
    print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))
