"""
    Problem Statement #
    Given an array containing 0s, 1s and 2s, sort the array in-place.
    You should treat numbers of the array as objects,
    hence, we can’t count 0s, 1s, and 2s to recreate the array.

    The flag of the Netherlands consists of three colors: red, white and blue;
    and since our input array also consists of three different numbers that is
    why it is called Dutch National Flag problem.


    Example 1:
    Input: [1, 0, 2, 1, 0]
    Output: [0 0 1 1 2]
        *
    0   0   1   1   2
            ^
    Example 2:
    Input: [2, 2, 0, 1, 2, 0]
    Output: [0 0 1 2 2 2 ]
"""


def dutch_national_flag(arr: [int]) -> [int]:
    size = len(arr) - 1

    for i in range(size):
        front = i + 1
        back = i
        while front <= size and back >= 0:
            if arr[back] > arr[front]:
                arr[front], arr[back] = arr[back], arr[front]
                back, front = back - 1, front - 1
            else:
                break
    return arr


if __name__ == '__main__':
    print(dutch_national_flag([1, 0, 2, 1, 0]))  # [0 0 1 1 2]
    print(dutch_national_flag([2, 2, 0, 1, 2, 0]))  # [0 0 1 2 2 2 ]
