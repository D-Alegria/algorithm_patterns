"""
    Quadruple Sum to Target (medium)
    Given an array of unsorted numbers and a target number,
    find all unique quadruplets in it,
    whose sum is equal to the target number.

    Example 1:
    Input: [4, 1, 2, -1, 1, -3], target=1
    Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
    Explanation: Both the quadruplets add up to the target.

    # 2, -1 = 3
    *
    -3  -1  1   1   2   4
                        ^
    A + B + X + Y = T
    X + Y = T - (A + B)

    Example 2:
    Input: [2, 0, -1, 1, -2, 2], target=2
    Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
    Explanation: Both the quadruplets add up to the target.
"""

from typing import List


def quadruple_sum_to_target(arr: List[int], target: int) -> List[List[int]]:
    arr.sort()
    result = []

    for i in range(len(arr) - 3):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        for j in range(i + 1, len(arr) - 2):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue
            back, front = j + 1, len(arr) - 1
            equator = target - arr[i] - arr[j]
            while back < front:
                if arr[back] + arr[front] < equator:
                    back += 1
                elif arr[back] + arr[front] > equator:
                    front -= 1
                else:
                    result.append([arr[i], arr[back], arr[front], arr[j]])
                    back += 1
                    front -= 1
                    while back < front and arr[back] == arr[back - 1]:
                        back += 1
                    while back < front and arr[front] == arr[front + 1]:
                        front -= 1
    return result


if __name__ == '__main__':
    print(quadruple_sum_to_target([4, 1, 2, -1, 1, -3], 1))  # [-3, -1, 1, 4], [-3, 1, 1, 2]
    print(quadruple_sum_to_target([2, 0, -1, 1, -2, 2], 2))  # [-2, 0, 2, 2], [-1, 0, 1, 2]
