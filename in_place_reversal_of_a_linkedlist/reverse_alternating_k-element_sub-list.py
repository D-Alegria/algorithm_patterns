"""
    Given the head of a LinkedList and a number ‘k’,
    reverse every alternating ‘k’ sized sub-list starting from the head.

    If, in the end, you are left with a sub-list with less than ‘k’ elements,
    reverse it too.
                                    p       c
    n   >   2   >   1   >   3   >   4   >   5   >   6   >   7   >   8   >   n
                    e       s
"""


class Node:

    def __init__(self, value: int, next_node=None):
        self.value = value
        self.next_node = next_node

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next_node
        print()


def reverse_alternate_k_elements(head_node: Node, k: int) -> Node:  # S = O(1) T = O(N)
    current = head_node
    prev = None
    while current is not None:
        last_of_prev_list = prev
        last_of_current_list = current
        i = 0
        while current is not None and i < k:
            next_node = current.next_node
            current.next_node = prev
            prev = current
            current = next_node
            i += 1

        if last_of_prev_list is not None:
            last_of_prev_list.next_node = prev
        else:
            head_node = prev
        last_of_current_list.next_node = current
        prev = last_of_current_list

        i = 0
        while current is not None and i < k:
            prev = current
            current = current.next_node
            i += 1

    return head_node


if __name__ == '__main__':
    head = Node(1)
    head.next_node = Node(2)
    head.next_node.next_node = Node(3)
    head.next_node.next_node.next_node = Node(4)
    head.next_node.next_node.next_node.next_node = Node(5)
    head.next_node.next_node.next_node.next_node.next_node = Node(6)
    head.next_node.next_node.next_node.next_node.next_node.next_node = Node(7)
    head.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(8)

    print("Original LinkedList are: ", end=" ")
    head.print_list()
    result = reverse_alternate_k_elements(head, 2)
    print("Reversed LinkedList are: ", end=" ")
    result.print_list()
