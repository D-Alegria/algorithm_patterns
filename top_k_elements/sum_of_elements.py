"""
    Given an array, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.

    Example 1:
    Input: [1, 3, 12, 5, 15, 11], and K1=3, K2=6
    Output: 23
    Explanation: The 3rd smallest number is 5 and 6th smallest number 15. The sum of numbers coming
    between 5 and 15 is 23 (11+12).


    1   3   12  5   15  11
        !
    1   3  12  5   15  11
                    ^
                    !
    1   3   11  5   12  15
                    ^
            k1          k2
    1   3   11  5   12  15  17  18

         p = 4
         p < k1
         p > k2 - 1


    [1,3,5,11,12,15]

    Example 2:
    Input: [3, 5, 8, 7], and K1=1, K2=4
    Output: 12
    Explanation: The sum of the numbers between the 1st smallest number (3) and the 4th smallest
    number (8) is 12 (5+7).


"""

from random import randint


def getPivot(start, end, nums):
    pivot_point = randint(start, end)
    nums[end], nums[pivot_point] = nums[pivot_point], nums[end]
    pointer = start

    for i in range(start, end):
        if nums[i] <= nums[end]:
            nums[i], nums[pointer] = nums[pointer], nums[i]
            pointer += 1

    nums[pointer], nums[end] = nums[end], nums[pointer]
    return pointer


def find_sum_of_elements(nums, k1, k2):
    n = len(nums)
    start, end = 0, n - 1

    while start < end:
        p = getPivot(start, end, nums)

        if p < k1:
            start = p + 1
        elif p > k1:
            end = p - 1
        else:
            break

    start, end = k1, n - 1
    while start < end:
        p = getPivot(start, end, nums)

        if p < k2 - 1:
            start = p + 1
        elif p > k2 - 1:
            end = p - 1
        else:
            break
    return sum(nums[k1:k2 - 1])


if __name__ == '__main__':
    print(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6))
    print(find_sum_of_elements([3, 5, 8, 7], 1, 4))
    