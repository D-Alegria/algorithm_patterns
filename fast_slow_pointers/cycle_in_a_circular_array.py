"""
    Cycle in a Circular Array (hard) #
    We are given an array containing positive and negative numbers.
    Suppose the array contains a number ‘M’ at a particular index.
    Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’ indices.
    You should assume that the array is circular which means two things:

    If, while moving forward, we reach the end of the array,
    we will jump to the first element to continue the movement.

    If, while moving backward, we reach the beginning of the array,
    we will jump to the last element to continue the movement.

    Write a method to determine if the array has a cycle.
    The cycle should have more than one element and should follow one direction
    which means the cycle should not contain both forward and backward movements.

    Example 1:
    Input: [1, 2, -1, 2, 2]
    Output: true
    Explanation: The array has a cycle among indices: 0 -> 1 -> 3 -> 0
    seen = 0,1,3,

    *
    1   2   -1  2   2

    Example 2:
    Input: [2, 2, -1, 2]
    Output: true
    Explanation: The array has a cycle among indices: 1 -> 3 -> 1
    seen = 0, 1, 3, 1
        *
    2   2   -1  2

    Example 3:
    Input: [2, 1, -1, -2]
    Output: false
    Explanation: The array does not have any cycle.
    seen = 0, 2, 1, 2
    *
    2   1   -1  -2
"""
from typing import List


def circular_array_loop_exists(nums: List[int]) -> bool:
    seen = set()  # 0
    size = len(nums)
    curr = 0
    quotient = 0
    while curr not in seen:  # 0
        seen.add(curr)
        quotient = curr + nums[curr]  # -1
        curr = quotient % size

    if quotient >= size:
        if size % 2 == 0:
            return curr < size // 2
        else:
            return curr <= size // 2
    else:
        if size % 2 == 0:
            return curr < size // 2
        else:
            return curr <= size // 2


if __name__ == '__main__':
    print(circular_array_loop_exists([1, 2, -1, 2, 2]))  # True
    print(circular_array_loop_exists([2, 2, -1, 2]))  # True
    print(circular_array_loop_exists([2, 1, -1, -2]))  # False
    print(circular_array_loop_exists([-1, 2]))  # False
    print(circular_array_loop_exists([1, 1, 2]))  # True
    print(circular_array_loop_exists([-1, -2, -3, -4, -5]))  # False
    print(circular_array_loop_exists([3, 1, 2]))  # True
