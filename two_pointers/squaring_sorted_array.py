"""
    Problem Statement #
    Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

    Example 1:
    Input: [-2, -1, 0, 2, 3]
    Output: [0, 1, 4, 4, 9]
            *
    -2  -1  0   2   3
            ^
    Example 2:
    Input: [-3, -1, 0, 1, 2]
    Output: [0 1 1 4 9]
"""


def squaring_sorted_array(arr: [int]) -> [int]:
    result = [0] * len(arr)
    front = len(arr) - 1
    back = 0

    for i in range(len(arr) - 1, 0, -1):
        if front == back:
            break
        if abs(arr[front]) >= abs(arr[back]):
            result[i] = arr[front] ** 2
            front -= 1
        else:
            result[i] = arr[back] ** 2
            back += 1
    return result


if __name__ == '__main__':
    print(squaring_sorted_array([-2, -1, 0, 2, 3]))  # [0, 1, 4, 4, 9]
    print(squaring_sorted_array([-3, -1, 0, 1, 2]))  # [0 1 1 4 9]
