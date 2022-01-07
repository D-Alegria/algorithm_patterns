"""
    Given a string, sort it based on the decreasing frequency of its characters.

    Example 1:
    Input: "Programming"
    Output: "rrggmmPiano"
    Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear before any other character.

    Example 2:
    Input: "abcbab"
    Output: "bbbaac"
    Explanation: 'b' appeared three times, 'a' appeared twice, and 'c' appeared only once.
"""

from collections import Counter
from heapq import *


def frequency_sort(s):
    count_map = Counter(s)
    max_heap = []

    for k, v in count_map.items():
        heappush(max_heap, (-v, k))

    result = []
    while max_heap:
        v, k = heappop(max_heap)
        result.extend(k * -v)
    return ''.join(result)


def frequency_sort1(s):
    count_map = Counter(s)
    s = list(s)

    for letter in count_map.keys():
        pivot_element = letter
        pivot_point = 0
        for i in range(0, len(s) - 1):
            if count_map[s[i]] >= count_map[pivot_element]:
                s[i], s[pivot_point] = s[pivot_point], s[i]
                pivot_point += 1
        s[pivot_point], s[-1] = s[-1], s[pivot_point]

    return ''.join(s)


if __name__ == '__main__':
    print(frequency_sort("Programming"))
    print(frequency_sort("abcbab"))
