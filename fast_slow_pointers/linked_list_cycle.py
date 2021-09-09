"""
    Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.

"""


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


def find_cycle(head: Node) -> bool:
    fast, slow = head, head

    while fast is not None and fast.next_node is not None:
        fast = fast.next_node.next_node
        slow = slow.next_node

        if fast == slow:
            return True
    return False


if __name__ == '__main__':
    head = Node(1)
    head.next_node = Node(2)
    head.next_node.next_node = Node(3)
    head.next_node.next_node.next_node = Node(4)
    head.next_node.next_node.next_node.next_node = Node(5)
    head.next_node.next_node.next_node.next_node.next_node = Node(6)
    print("Linked has cycle: " + str(find_cycle(head)))

    head.next_node.next_node.next_node.next_node.next_node = head.next_node.next_node
    print("Linked has cycle: " + str(find_cycle(head)))

    head.next_node.next_node.next_node.next_node.next_node = head.next_node.next_node.next_node
    print("Linked has cycle: " + str(find_cycle(head)))
