"""
    Problem Statement
    Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

    Example 1:
    Input: [-3, 0, 1, 2, -1, 1, -2]
    Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
    Explanation: There are four unique triplets whose sum is equal to zero.

    *
    -3  0   1   2   -1  1   -2
                    ^
    3
            *
    -3  -2  -1  0   1   1   2
                            ^
    Example 2:
    Input: [-5, 2, -1, -2, 3]
    -5, -2, -1, 2, 3
    Output: [[-5, 2, 3], [-2, -1, 3]]
    Explanation: There are two unique triplets whose sum is equal to zero.
"""


def triple_to_zero1(arr: [int]) -> [[int]]:
    result = []
    arr = sorted(arr)  # N Log N

    for i, val in enumerate(arr):  # N
        front = len(arr) - 1
        back = 0
        equator = -val
        while back < front:  # N
            # if the index is the same continue
            if i == back:
                back += 1
                continue
            if i == front:
                front -= 1
                continue
            if arr[back] + arr[front] < equator:
                back += 1
            elif arr[back] + arr[front] > equator:
                front -= 1
            else:
                sub_result = sorted([val, arr[back], arr[front]])  # 3 Log 3
                if sub_result not in result:  # N
                    result.append(sub_result)
                back += 1
                front -= 1
    return result


def triple_to_zero(arr: [int]) -> [[int]]:
    result = []
    arr = sorted(arr)  # N Log N

    for i, val in enumerate(arr):  # N
        front = len(arr) - 1
        back = i
        equator = -val
        while back < front and arr[back] != arr[back - 1]:  # N
            # if the index is the same continue
            if i == back:
                back += 1
                continue
            if i == front:
                front -= 1
                continue
            if arr[back] + arr[front] < equator:
                back += 1
            elif arr[back] + arr[front] > equator:
                front -= 1
            else:
                result.append([val, arr[back], arr[front]])
                back += 1
                front -= 1
    return result


if __name__ == '__main__':
    print(triple_to_zero([-3, 0, 1, 2, -1, 1, -2]))  # [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
    print(triple_to_zero([-5, 2, -1, -2, 3]))  # [[-5, 2, 3], [-2, -1, 3]]
