import time

"""
    Given an array of positive numbers and a positive number ‘k’, find the maximum
    sum of any contiguous sub array of size ‘k’.

    Example
    Input: [2, 1, 5, 1, 3, 2], k=3
    Output: 9
    Explanation: Subarray with maximum sum is [5, 1, 3].
"""


def max_sum_sub_array1(k, arr):
    max_sum = 0
    end = 0
    for i in range(k, len(arr)):
        max_sum = max(max_sum, sum(arr[end:i]))
        end += 1
    return max_sum


def max_sum_sub_array2(k, arr):
    max_sum = 0
    window = 0
    for ind, num in enumerate(arr):
        window += num
        if ind >= k - 1:
            max_sum = max(max_sum, window)
            window -= arr[ind - 2]
    return max_sum


time1 = 0
time2 = 0
testAmount = 10000000
if __name__ == '__main__':
    start = time.time()
    time.sleep(1)
    print(max_sum_sub_array1(3, [2, 1, 5, 1, 3, 2]))
    time.sleep(1)
    end = time.time()
    time1 = end - start
    start = time.time()
    time.sleep(1)
    print(max_sum_sub_array2(3, [2, 1, 5, 1, 3, 2]))
    time.sleep(1)
    end = time.time()
    time2 = end - start

    print("Average of Function 1: %s" % time1)
    print("Average of Function 2: %s" % time2)

    print("Minimum %s" % (min(time1, time2)))
    print("Maximum %s" % (max(time1, time2)))
