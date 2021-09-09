"""
    Problem Statement #
    Given the head of a Singly LinkedList that contains a cycle,
    write a function to find the starting node of the cycle.

"""
from length_of_cycle import length_of_cycle


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


def start_of_cycle(head_node: Node) -> Node:  # T = O(3N);  S = O(1)
    fast, slow = head_node, head_node
    length = length_of_cycle(head_node)  # N

    for i in range(length - 1):  # N
        fast = fast.next_node

    while fast != slow:  # N
        fast = fast.next_node
        slow = slow.next_node

    return fast


if __name__ == '__main__':
    head = Node(1)
    head.next_node = Node(2)
    head.next_node.next_node = Node(3)
    head.next_node.next_node.next_node = Node(4)
    head.next_node.next_node.next_node.next_node = Node(5)
    head.next_node.next_node.next_node.next_node.next_node = Node(6)

    head.next_node.next_node.next_node.next_node.next_node = head.next_node.next_node
    print("Linked list start of cycle: " + str(start_of_cycle(head).value))  # True

    head.next_node.next_node.next_node.next_node.next_node = head.next_node.next_node.next_node
    print("Linked list start of cycle: " + str(start_of_cycle(head).value))  # True

    head.next_node.next_node.next_node.next_node.next_node = head
    print("Linked list start of cycle: " + str(start_of_cycle(head).value))  # True
