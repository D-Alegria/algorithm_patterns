"""
    Given a sorted array of numbers, find if a given number ‘key’ is present in the array.
    Though we know that the array is sorted,
    we don’t know if it’s sorted in ascending or descending order.
    You should assume that the array can have duplicates.

    Write a function to return the index of the ‘key’ if it is present in the array,
    otherwise return -1.

    Example 1:
    Input: [4, 6, 10], key = 10
    Output: 2

    Example 2:
    Input: [1, 2, 3, 4, 5, 6, 7], key = 5
    Output: 4

    Example 3:
    Input: [10, 6, 4], key = 10
    Output: 0

    Example 4:
    Input: [10, 6, 4], key = 4
    Output: 2

"""

"""
    2//2 1
    
"""


def binary_search(arr, key):
    start, end = 0, len(arr) - 1
    isAscending = arr[start] < arr[end]

    while start <= end:
        mid = (start + end) // 2
        if isAscending:
            if arr[mid] < key:
                start = mid + 1
            elif arr[mid] > key:
                end = mid - 1
            else:
                return mid
        else:
            if arr[mid] > key:
                start = mid + 1
            elif arr[mid] < key:
                end = mid - 1
            else:
                return mid


if __name__ == '__main__':
    print(binary_search([4, 6, 10], 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    print(binary_search([10, 6, 4], 10))
    print(binary_search([10, 6, 4], 4))
