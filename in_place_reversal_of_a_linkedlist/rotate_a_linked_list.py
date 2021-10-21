"""
    Rotate a LinkedList (medium) #
    Given the head of a Singly LinkedList and a number ‘k’,
    rotate the LinkedList to the right by ‘k’ nodes.

    Example 1:
    k = 3
    Original list = 1   >   2   >   3   >   4   >   5   >   6   >   n
    Rotated list =  4   >   5   >   6   >   1   >   2   >   3   >   n

    Example 2:
    k = 8
    Original list = 1   >   2   >   3   >   4   >   5   >   n
    Rotated list =  3   >   4   >   5   >   1   >   2   >   n

                    p       c               t
    1   >   2   >   3   >   4   >   5   >   6   >   n
    h

    tail.next = head
    head = c
    p.next = null
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


def rotate(head_node: Node, rotation: int) -> Node:  # S = O(1) T = O(N)
    # iterate to the end of linked list and get the length
    tail = head_node
    length = 1
    while tail.next_node is not None:
        tail = tail.next_node
        length += 1
    # get the part to rotate
    length_to_rotate = rotation % length
    current = head_node
    prev = None
    i = 0
    while current is not None and i < length_to_rotate:
        prev = current
        current = current.next_node
        i += 1

    # rotate
    tail.next_node = head_node
    head_node = current
    prev.next_node = None

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
    result = rotate(head, 3)
    print("Reversed LinkedList are: ", end=" ")
    result.print_list()
