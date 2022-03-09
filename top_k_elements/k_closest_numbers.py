"""
    Given a sorted number array and two integers ‘K’ and ‘X’,
    find ‘K’ closest numbers to ‘X’ in the array.
    Return the numbers in the sorted order.
    ‘X’ is not necessarily present in the array.

    Example 1:
    Input: [5, 6, 7, 8, 9], K = 3, X = 7
    Output: [6, 7, 8]

    Example 2:
    Input: [2, 4, 5, 6, 9], K = 3, X = 6
    Output: [4, 5, 6]

    Example 3:
    Input: [2, 4, 5, 6, 9], K = 3, X = 10
    Output: [5, 6, 9]
                !
    9   6   5   4   2
            ^
"""
import heapq
import random


def binary_search(arr, X):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] < X:
            start = mid + 1
        elif arr[mid] > X:
            end = mid - 1
        else:
            return mid
    return end


def find_closest_elements1(arr, K, X):
    index = binary_search(arr, X)
    start, end = index - K, index + K

    start = max(start, 0)
    end = min(end, len(arr) - 1)

    minHeap = []

    for i in range(start, end + 1):
        heapq.heappush(minHeap, (abs(arr[i] - X), arr[i]))

    result = []
    for _ in range(K):
        result.append(heapq.heappop(minHeap)[1])

    result.sort()
    return result


def get_pivot_point(start, end, X, arr):
    pivot_point = random.randint(start, end)
    arr[end], arr[pivot_point] = arr[pivot_point], arr[end]
    pointer = start

    for i in range(start, end):
        if abs(X - arr[i][1]) < abs(X - arr[end][1]):
            arr[pointer], arr[i] = arr[i], arr[pointer]
            pointer += 1

    arr[pointer], arr[end] = arr[end], arr[pointer]
    return pointer


def find_closest_elements(arr, K, X):
    result = list(arr)
    arr = [(idx, val) for idx, val in enumerate(arr)]

    # using quick select - sort the value in the arr based on the diff from X
    n = len(arr)
    start, end = 0, n - 1
    while start < end:
        p = get_pivot_point(start, end, X, arr)
        if p > K - 1:
            end = p - 1
        elif p < K - 1:
            start = p + 1
        else:
            break

    mini, maxi = n, -1
    for i in range(K):
        mini = min(mini, arr[i][0])
        maxi = max(maxi, arr[i][0])

    return result[mini:maxi + 1]


if __name__ == '__main__':
    print("'K' closest numbers to 'X' are: " + str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: " + str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " + str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))
