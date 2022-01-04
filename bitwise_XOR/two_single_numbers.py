"""
    In a non-empty array of numbers,
    every number appears exactly twice except two numbers that appear only once.
    Find the two numbers that appear only once.

    Example 1:
    Input: [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
    Output: [4, 6]

    Example 2:
    Input: [2, 1, 3, 2]
    Output: [1, 3]
"""


def find_single_numbers(arr):
    n1xn2 = 0
    for i in arr:
        n1xn2 ^= i

    rightmost_set_bit = 1
    while rightmost_set_bit & n1xn2 == 0:
        rightmost_set_bit = rightmost_set_bit << 1
    n1, n2 = 0, 0

    for num in arr:
        if num & rightmost_set_bit != 0:
            n1 ^= num
        else:
            n2 ^= num

    return [n1, n2]


if __name__ == '__main__':
    print(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5]))
    print(find_single_numbers([2, 1, 3, 2]))
