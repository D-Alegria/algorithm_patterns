import math

"""
    Given an array of positive numbers and a positive
    number ‘S’, find the length of the smallest contiguous
    subarray whose sum is greater than or equal to ‘S’.
    Return 0, if no such subarray exists.

    Input: [2, 1, 5, 2, 3, 2], S=7
    Output: 2
    Explanation: The smallest subarray with a sum great
    than or equal to '7' is [5, 2].
"""


def small_sub_array(S, arr):
    min_win, window, size, start = math.inf, 0, 0, 0

    for ind, end in enumerate(arr):
        window += end
        size += 1
        if window >= S:
            min_win = min(min_win, size)
            print(min_win)
            while window >= S:
                window -= arr[start]
                size -= 1
                start += 1
    if window < S:
        return 0
    else:
        return min_win


if __name__ == '__main__':
    print(small_sub_array(7, [2, 1, 5, 2, 3, 2]))
