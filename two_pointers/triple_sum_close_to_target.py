"""
    Problem Statement #
    Given an array of unsorted numbers and a target number,
    find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet.
    If there are more than one such triplet, return the sum of the triplet with the smallest sum.

    Example 1:
    Input: [-2, 0, 1, 2], target=2
    Output: 1
    Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

    -2 + X + Y -> 2
    X + Y -> 2 - (-2) = 4

            *
    -2  0   1   2
                ^
    0 + 2 = 2       < 4
    1 + 2 = 3       < 4


    Example 2:
    Input: [-3, -1, 1, 2], target=1
    Output: 0
    Explanation: The triplet [-3, 1, 2] has the closest sum to the target.

    Example 3:
    Input: [1, 0, 1, 1], target=100
    Output: 3
    Explanation: The triplet [1, 1, 1] has the closest sum to the target.
    *
    1   0   1   1
                ^
"""
import math


def close_to_target(arr: [int], target: int) -> int:
    arr.sort()
    minimum_sum = -math.inf

    for i, val in enumerate(arr):
        front = len(arr) - 1
        back = 0
        equator = target - val
        while back < front and arr[i] != arr[i - 1]:
            if back == i:
                back += 1
            if front == i:
                front -= 1
            if arr[back] + arr[front] < equator:
                minimum_sum = max(minimum_sum, val + arr[back] + arr[front])
                back += 1
            elif arr[back] + arr[front] > equator:
                front -= 1
            else:
                front -= 1
                back += 1
    return minimum_sum


if __name__ == '__main__':
    print(close_to_target([-2, 0, 1, 2], 2))  # 1
    print(close_to_target([-3, -1, 1, 2], 2))  # 0
    print(close_to_target([1, 0, 1, 1], 100))  # 3
