"""
    Given an array of numbers sorted in ascending order,
    find the range of a given number ‘key’.
    The range of the ‘key’ will be the first and last position of the ‘key’ in the array.

    Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].

    Example 1:
    Input: [4, 6, 6, 6, 9], key = 6
    Output: [1, 3]

    Example 2:
    Input: [1, 3, 8, 10, 15], key = 10
    Output: [3, 3]

    Example 3:
    Input: [1, 3, 8, 10, 15], key = 12
    Output: [-1, -1]
"""


def find_range1(arr, key):
    result = [-1, -1]
    start, end = 0, len(arr) - 1

    while start < end:
        mid = start + (end - start) // 2

        if arr[mid] < key:
            start = mid + 1
        elif arr[mid] > key:
            end = mid - 1
        else:
            start, end = mid, mid
            while start > 0 and arr[start - 1] == key:
                start -= 1
            while end < len(arr) - 1 and arr[end + 1] == key:
                end += 1
            return [start, end]
    return result


def binary_search(arr, key, findMax):
    start, end = 0, len(arr) - 1
    keyIndex = -1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] < key:
            start = mid + 1
        elif arr[mid] > key:
            end = mid - 1
        else:
            keyIndex = mid
            if findMax:
                start = mid + 1
            else:
                end = mid - 1
    return keyIndex


def find_range(arr, key):
    result = [-1, -1]
    result[0] = binary_search(arr, key, False)
    if result[0] != -1:
        result[1] = binary_search(arr, key, True)
    return result


if __name__ == '__main__':
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))
