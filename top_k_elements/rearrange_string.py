"""
    Given a string, find if its letters can be rearranged in such a way that no two same
    characters come next to each other.

    Example 1:
    Input: "aappp"
    Output: "papap"
    Explanation: In "papap", none of the repeating characters come next to each other.

    p:3 a:2

    p a p a p

    Example 2:
    Input: "Programming"
    Output: "rgmrgmPiano" or "gmringmrPoa" or "gmrPagimnor", etc.
    Explanation: None of the repeating characters come next to each other.

    p:1 r:2 o:1 g:2 a:1 m:2 i:1 n:1

    r:2 g:2 m:2 p:1 o:1 a:1 i:1 n:1

    rgmpoainrgm

    Example 3:
    Input: "aapa"
    Output: ""
    Explanation: In all arrangements of "aapa", atleast two 'a' will come together e.g., "apaa", "paaa".

    a:3 p:1
    ap
"""

from collections import Counter
from heapq import heappop, heappush


def rearrange_string(s):
    count = Counter(s)
    store = []

    for v, c in count.items():
        heappush(store, (-c, v))

    result = []
    while store:
        c, v = heappop(store)
        c = -c
        if result and v == result[-1]:
            return ""
        result.append(v)
        c -= 1
        if c > 0:
            heappush(store, (-c, v))

    return "".join(result)


if __name__ == '__main__':
    print(rearrange_string("aappp"))
    print(rearrange_string("Programming"))
    print(rearrange_string("aapa"))
