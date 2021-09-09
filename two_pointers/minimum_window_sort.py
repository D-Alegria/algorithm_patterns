"""
    Minimum Window Sort (medium) #
    Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

    Example 1:
    Input: [1, 2, 5, 3, 7, 10, 9, 12]
    Output: 5
    Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted
        *
    1   2   5   3   7   10  9   12
                            ^
    0
    6
    Example 2:
    Input: [1, 3, 2, 0, -1, 7, 10]
    Output: 5
    Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted
                    *
    1   3   2   0   -1  7   10
        ^
    Example 3:
    Input: [1, 2, 3]
    Output: 0
    Explanation: The array is already sorted

    Example 4:
    Input: [3, 2, 1]
    Output: 3
    Explanation: The whole array needs to be sorted.
"""
import math


def minimum_window(arr: [int]) -> int:
    front, back = len(arr) - 1, 0
    mini = math.inf
    maxi = -math.inf

    for i in range(1, len(arr) - 1):
        if arr[i] < arr[i - 1]:
            if arr[i] < mini:
                back = i
            mini = min(mini, arr[i])
    # print(mini)

    for i in range(len(arr) - 2, 0, -1):
        if arr[i] > arr[i + 1]:
            if arr[i] > maxi:
                front = i + 1
            maxi = max(maxi, arr[i])
    # print(maxi)

    while back > 0 and  mini < arr[back - 1]:
        back -= 1
    # print(back)

    while front <= len(arr) - 1 and maxi > arr[front]:
        front += 1
    # print(front)
    if abs(maxi - mini) == math.inf:
        return 0
    else:
        return front - back


if __name__ == '__main__':
    print(minimum_window([1, 2, 5, 3, 7, 10, 9, 12]))  # 5
    print(minimum_window([1, 3, 2, 0, -1, 7, 10]))  # 5
    print(minimum_window([1, 2, 3]))  # 0
    print(minimum_window([3, 2, 1]))  # 3
