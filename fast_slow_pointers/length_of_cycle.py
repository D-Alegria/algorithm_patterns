"""
    Problem 1: Given the head of a LinkedList with a cycle, find the length of the cycle.
"""


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


def length_of_cycle(head_node: Node) -> int:
    fast, slow, length = head_node, head_node, 1

    while fast is not None and fast.next_node is not None:
        fast = fast.next_node.next_node
        slow = slow.next_node

        if fast == slow:
            current = slow
            while True:
                current = current.next_node
                length += 1
                if current == slow:
                    break
            return length

    return 0


if __name__ == '__main__':
    head = Node(1)
    head.next_node = Node(2)
    head.next_node.next_node = Node(3)
    head.next_node.next_node.next_node = Node(4)
    head.next_node.next_node.next_node.next_node = Node(5)
    head.next_node.next_node.next_node.next_node.next_node = Node(6)
    print("Linked has cycle length: " + str(length_of_cycle(head)))  # 0

    head.next_node.next_node.next_node.next_node.next_node = head.next_node.next_node
    print("Linked has cycle length: " + str(length_of_cycle(head)))  # 4

    head.next_node.next_node.next_node.next_node.next_node = head.next_node.next_node.next_node
    print("Linked has cycle length: " + str(length_of_cycle(head)))  # 3
