"""
    Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s,
    find the length of the longest contiguous subarray having all 1s.

    Example 1:
    Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
    Output: 6
    Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

    Example 2:
    Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
    Output: 9
    Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.

    Algorithm
    have a window for the longest 1's founds with k substitutes
    increase the window as we go
    and decrease if our window is too large ie it's longer than the longest 1's + k substitutes

"""


def longest_ones(arr: [], k: int) -> int:
    window, longest_one, largest = 0, 0, 0

    for i, val in enumerate(arr):
        window += 1
        longest_one += val

        while window > longest_one + k:
            window -= 1
            if arr[i - window] == 1:
                longest_one -= 1
        largest = max(window, largest)
    return largest


if __name__ == '__main__':
    print(longest_ones([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))  # 6
    print(longest_ones([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))  # 9
