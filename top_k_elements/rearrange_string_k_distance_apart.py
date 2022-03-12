"""
    Rearrange String K Distance Apart (hard)
    Given a string and a number ‘K’, find if the string can be rearranged
    such that the same characters are at least ‘K’ distance apart from each
    other.

    Example 1:
    Input: "mmpp", K=2
    Output: "mpmp" or "pmpm"
    Explanation: All same characters are 2 distance apart.
            !
    {m:2, p:2}
    [2,m][2,p] k = 2
    [1,m][1,p] k = 2
    result = [m,p,m,p]

    aa

    Example 2:
    Input: "Programming", K=3
    Output: "rgmPrgmiano" or "gmringmrPoa" or "gmrPagimnor" and a few more
    Explanation: All same characters are 3 distance apart.

    {p:1,r:2,o:1,g:2,a:1,m:2,i:1,n:1}
    (2,g),(r,2),(m,2),(p,1,(o,1),(a,1),(i,1),(n,1)

    g,r,m,p,o,i,n,g,r,m

    Example 3:
    Input: "aab", K=2
    Output: "aba"
    Explanation: All same characters are 2 distance apart.

    {a:2,b:1}




    Example 4:
    Input: "aapa", K=3
    Output: ""
    Explanation: We cannot find an arrangement of the string where any two 'a' are 3 distance apart.

    aapac
    a:3, p:2
    heap
    queue (0,c)(1,a),(0,p)
    a,p,c,a,p
"""

from collections import Counter, deque
from heapq import heappush, heappop


def rearrange_string_k_distance_apart(s, k):
    counter = Counter(s)
    maxHeap = []
    queue = deque()

    for v, c in counter.items():
        heappush(maxHeap, (-c, v))

    result = []
    while maxHeap:
        c, v = heappop(maxHeap)
        result.append(v)
        c += 1

        queue.append((c, v))
        if len(queue) == k:
            c, v = queue.popleft()
            if -c > 0:
                heappush(maxHeap, (c, v))

    return "".join(result) if len(result) == len(s) else ""


if __name__ == '__main__':
    print("Reorganized string: " + rearrange_string_k_distance_apart("mmpp", 2))
    print("Reorganized string: " + rearrange_string_k_distance_apart("Programming", 3))
    print("Reorganized string: " + rearrange_string_k_distance_apart("aab", 2))
    print("Reorganized string: " + rearrange_string_k_distance_apart("aapa", 3))
