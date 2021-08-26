"""
    Problem Statement #
    Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

    Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

    Example 1:
    Input: [1, 2, 3, 4, 6], target=6
    Output: [1, 3]
    Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

    Example 2:
    Input: [2, 5, 9, 11], target=11
    Output: [0, 2]
    Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
"""
from typing import List


def pair_with_target_sum(arr: List[int], target: int) -> List[int]:
    front = len(arr) - 1
    back = 0

    for i in range(len(arr) - 1):
        if arr[front] + arr[back] > target:
            front -= 1
        elif arr[front] + arr[back] < target:
            back += 1
        elif arr[front] + arr[back] == target:
            return [back, front]
    return []


if __name__ == '__main__':
    print(pair_with_target_sum([1, 2, 3, 4, 6], 6))  # [1, 3]
    print(pair_with_target_sum([2, 5, 9, 11], 11))  # [0, 2]
