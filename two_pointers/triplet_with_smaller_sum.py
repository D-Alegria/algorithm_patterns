"""
    Problem Statement
    Given an array arr of unsorted numbers and a target sum, count all triplets in it such that
    arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices.
    Write a function to return the count of such triplets.

    Example 1:
    Input: [-1, 0, 2, 3], target=3
    Output: 2
    Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]
        *
    -1  0   2    3
                ^
    -1 + X + Y < T
    X + Y < T - (-1)

    Example 2:
    Input: [-1, 4, 2, 1, 3], target=5
    Output: 4
    Explanation: There are four triplets whose sum is less than the target:
    [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
"""
import math
from typing import List


def smaller_sum(arr: List[int], target: int) -> int:
    arr.sort()
    total = -math.inf

    for i, val in enumerate(arr):
        front = len(arr) - 1
        back = 0
        equator = target - val
        while back < front and arr[i] != arr[i - 1]:
            if arr[back] + arr[front] < equator:
                total = max(total, val + arr[back] + arr[front])
                back += 1
            elif arr[back] + arr[front] > equator:
                front -= 1
            else:
                back += 1
                front -= 1
    return total


if __name__ == '__main__':
    print(smaller_sum([-1, 0, 2, 3], 3))  # 2
    print(smaller_sum([-1, 4, 2, 1, 3], 5))  # 4
