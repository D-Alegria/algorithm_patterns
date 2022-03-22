"""
    Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.

    Example 1:
    Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
    Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]

    Example 2:
    Input: L1=[5, 8, 9], L2=[1, 7]
    Output: [1, 5, 7, 8, 9]
"""

from heapq import heappush, heappop


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __lt__(self, other):
        return self.value < other.value


def merge_lists(lists):
    head = None
    minHeap = []

    for li in lists:
        if li:
            heappush(minHeap, li)

    if not minHeap:
        return head

    prev = head = None
    while minHeap:
        node = heappop(minHeap)
        if not head:
            prev = head = node
        else:
            prev.next = node
            prev = prev.next
        if node.next:
            heappush(minHeap, node.next)
        print(minHeap)
    return head


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(8)

    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(4)

    result = merge_lists([l1, l2, l3])
    print("Here are the elements form the merge list: ", end='')
    while result:
        print(str(result.value) + " ", end='')
        result = result.next
