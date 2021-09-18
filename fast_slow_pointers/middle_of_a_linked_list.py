"""
    Problem Statement
    Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.

    If the total number of nodes in the LinkedList is even, return the second middle node.

    Example 1:
    Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
    Output: 3
                *
    1   2   3   4   5   6   7   n
                        ^
    Example 2:
    Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
    Output: 4

    Example 3:
    Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> null
    Output: 4
"""


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


def middle_linked_list(head_node: Node) -> Node:  # T = O(N), S = O(1)
    fast, slow = head_node, head_node

    while fast is not None and fast.next_node is not None:  # N
        fast = fast.next_node.next_node
        slow = slow.next_node
    return slow


if __name__ == '__main__':
    head = Node(1)
    head.next_node = Node(2)
    head.next_node.next_node = Node(3)
    head.next_node.next_node.next_node = Node(4)
    head.next_node.next_node.next_node.next_node = Node(5)
    print("Middle Node: " + str(middle_linked_list(head).value))
    head.next_node.next_node.next_node.next_node.next_node = Node(6)
    print("Middle Node: " + str(middle_linked_list(head).value))
    head.next_node.next_node.next_node.next_node.next_node.next_node = Node(7)
    print("Middle Node: " + str(middle_linked_list(head).value))
