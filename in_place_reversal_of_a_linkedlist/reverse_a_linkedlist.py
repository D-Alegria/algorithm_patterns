"""
    Given the head of a Singly LinkedList, reverse the LinkedList.
    Write a function to return the new head of the reversed LinkedList.
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


def reverse(head_node: Node) -> Node:
    prev = None
    while head_node is not None:
        next_node = head_node.next_node  # store next node
        head_node.next_node = prev  # switch pointer of current node next node to prev node
        prev = head_node  # move prev pointer forward
        head_node = next_node  # move head pointer forward
    return prev


if __name__ == '__main__':
    head = Node(2)
    head.next_node = Node(4)
    head.next_node.next_node = Node(6)
    head.next_node.next_node.next_node = Node(8)
    head.next_node.next_node.next_node.next_node = Node(10)

    print("Original LinkedList are: ", end=" ")
    head.print_list()
    result = reverse(head)
    print("Reversed LinkedList are: ", end=" ")
    result.print_list()
