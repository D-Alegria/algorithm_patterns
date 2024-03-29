"""
    Given an array of numbers sorted in ascending order,
    find the element in the array that has the minimum difference with the given ‘key’.

    Example 1:
    Input: [4, 6, 10], key = 7
    Output: 6
    Explanation: The difference between the key '7' and '6' is minimum than any other number in the array
    !
    4   6   10
        ^
    4 - 6 = -2


    Example 2:
    Input: [4, 6, 10], key = 4
    Output: 4

    4 - 6 == -2

    Example 3:
    Input: [1, 3, 8, 10, 15], key = 12
    Output: 10
        !
    1   3   8   10  15
        ^
    12 - 8 == 4

    12 - 10 == 2

    Example 4:
    Input: [4, 6, 10], key = 17
    Output: 10
"""


def search_min_diff_element(arr, key):
    start, end = 0, len(arr) - 1

    if key < arr[0]:
        return arr[0]
    if key > arr[end]:
        return arr[end]

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] < key:
            start = mid + 1
        elif arr[mid] > key:
            end = mid - 1
        else:
            return arr[mid]

    # print(f"start: {start}, end: {end}")
    if key - arr[start] > arr[end] - key:
        return arr[start]
    return arr[end]


if __name__ == '__main__':
    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([4, 6, 10], 4))
    print(search_min_diff_element([1, 3, 8, 10, 15], 12))
    print(search_min_diff_element([1, 3, 8, 10, 15], 7))
    print(search_min_diff_element([4, 6, 10], 17))
