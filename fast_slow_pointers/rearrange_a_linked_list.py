"""
    Rearrange a LinkedList (medium) #
    Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes from the second
    half of the LinkedList are inserted alternately to the nodes from the first half in reverse order.
    So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null,
    your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

    Your algorithm should not use any extra space and the input LinkedList should be modified in-place.

    Example 1:
    Input: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
    Output: 2 -> 12 -> 4 -> 10 -> 6 -> 8 -> null
                *   !
    2   4   6   8   10  12  n
                ^
        *
    2   4   6
    *
    12  10  8
    2   12  4
    t = 4

    Example 2:
    Input: 2 -> 4 -> 6 -> 8 -> 10 -> null
    Output: 2 -> 10 -> 4 -> 8 -> 6 -> null
"""


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next_node
        print()


def rearrange(head_node: Node) -> Node:
    fast, slow, b4_slow = head_node, head_node, None

    # find center
    while fast is not None and fast.next_node is not None:
        fast = fast.next_node.next_node
        b4_slow = slow
        slow = slow.next_node

    if fast is None:
        b4_slow.next_node = None
    fast = slow
    # reverse from the center to the end
    prev = None
    while fast is not None:
        next_node = fast.next_node
        fast.next_node = prev
        prev = fast
        fast = next_node

    fast = prev
    slow = head_node
    # mix fast and slow
    while fast is not None and slow is not None:
        temp = slow.next_node
        slow.next_node = fast
        slow, temp = temp, fast.next_node
        fast.next_node = slow
        fast = temp
    return head


if __name__ == '__main__':
    head = Node(2)
    head.next_node = Node(4)
    head.next_node.next_node = Node(6)
    head.next_node.next_node.next_node = Node(8)
    head.next_node.next_node.next_node.next_node = Node(10)
    head.next_node.next_node.next_node.next_node.next_node = Node(12)
    rearrange(head)
    head.print_list()

    head = Node(2)
    head.next_node = Node(4)
    head.next_node.next_node = Node(6)
    head.next_node.next_node.next_node = Node(8)
    head.next_node.next_node.next_node.next_node = Node(10)
    rearrange(head)
    head.print_list()
