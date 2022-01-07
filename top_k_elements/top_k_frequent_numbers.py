"""
    Given an unsorted array of numbers,
    find the top ‘K’ frequently occurring numbers in it.

    Example 1:
    Input: [1, 3, 5, 12, 11, 12, 11], K = 2
    Output: [12, 11]
    Explanation: Both '11' and '12' appeared twice.

    Example 2:
    Input: [5, 12, 11, 3, 11], K = 2
    Output: [11, 5] or [11, 12] or [11, 3]
    Explanation: Only '11' appeared twice, all other numbers appeared once.
"""
import random


def find_top_k_frequent_numbers(arr, k):
    k_map = {}

    for i in arr:
        if i not in k_map:
            k_map[i] = 0
        k_map[i] += 1

    return get_top_elements(k_map, list(k_map.keys()), k, 0, len(k_map.keys()) - 1)


def get_partition(k_map, arr, start, end):
    # 5, 11, 12, 1, 3
    pivot_element = random.randint(start, end)
    # pivot_element = end
    arr[pivot_element], arr[end] = arr[end], arr[pivot_element]
    pivot_point = start

    for i in range(start, end):
        if k_map[arr[i]] >= k_map[arr[pivot_element]]:
            arr[pivot_point], arr[i] = arr[i], arr[pivot_point]
            pivot_point += 1
    arr[pivot_point], arr[end] = arr[end], arr[pivot_point]
    return pivot_point


def get_top_elements(k_map, arr, k, start, end):
    # print(f"arr {arr} start {start} end {end}")
    p = get_partition(k_map, arr, start, end)
    # print(f"arr {arr} start {start} end {end} p {p} [2]")

    if p < k - 1:
        return get_top_elements(k_map, arr, k, p + 1, end)
    elif p > k - 1:
        return get_top_elements(k_map, arr, k, start, p - 1)
    return arr[:k]


if __name__ == '__main__':
    print(find_top_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2))
    print(find_top_k_frequent_numbers([5, 12, 11, 3, 11], 2))
