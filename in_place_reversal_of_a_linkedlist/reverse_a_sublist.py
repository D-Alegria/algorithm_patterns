"""
    Given the head of a LinkedList and two positions ‘p’ and ‘q’,
    reverse the LinkedList from position ‘p’ to ‘q’.
                                    @       h
    n   >   1   <   2   <   3   <   4   >   5   >   n
                                            ^
    p = 2
    q = 4
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


def reverse_sub_list(head_node: Node, p: int, q: int) -> Node:  # S= O(1) T = O(N)
    prev = None
    save_head = head_node
    # move to start of sublist
    while head_node is not None and head_node.value != p:  # O(N)
        prev = head_node
        head_node = head_node.next_node

    # store prev and current head
    start = prev
    sublist_start = head_node

    # reverse the list
    while prev.value != q:  # O(N)
        next_node = head_node.next_node
        head_node.next_node = prev
        prev = head_node
        head_node = next_node

    start.next_node = prev
    sublist_start.next_node = head_node

    return save_head


if __name__ == '__main__':
    head = Node(1)
    head.next_node = Node(2)
    head.next_node.next_node = Node(3)
    head.next_node.next_node.next_node = Node(4)
    head.next_node.next_node.next_node.next_node = Node(5)

    print("Original LinkedList are: ", end=" ")
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Reversed LinkedList are: ", end=" ")
    result.print_list()
