"""
    Palindrome LinkedList (medium) #
    Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

    Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm
    is finished. The algorithm should have O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.

    Example 1:
    Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
    Output: true
            *
    2   4   6   4   2
            ^
    h n
    n n
    p 2
    Example 2:
    Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
    Output: false
"""


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


def check_palindrome(head_node: Node) -> bool:
    fast, slow, l = head_node, head_node, None

    # get to the middle of the linked ist
    while fast is not None and fast.next_node is not None:
        fast = fast.next_node.next_node
        prev = l
        l = slow
        slow = slow.next_node
        l.next_node = prev

    if fast is None:  # even
        fast = slow
    else:  # odd
        fast = slow
        fast = fast.next_node

    # check if nodes are equal and reverse
    result = True
    while l is not None:
        next_node = slow
        slow = l
        l = l.next_node
        slow.next_node = next_node
        if fast.value != slow.value:
            result = False
        fast = fast.next_node
    return result


if __name__ == '__main__':
    head = Node(2)
    head.next_node = Node(4)
    head.next_node.next_node = Node(6)
    head.next_node.next_node.next_node = Node(4)
    head.next_node.next_node.next_node.next_node = Node(2)
    print("Is Palindrome: " + str(check_palindrome(head)))  # True
    head.next_node.next_node.next_node.next_node.next_node = Node(2)
    print("Is Palindrome: " + str(check_palindrome(head)))  # False

    head2 = Node(1)
    head2.next_node = Node(2)
    head2.next_node.next_node = Node(4)
    head2.next_node.next_node.next_node = Node(4)
    head2.next_node.next_node.next_node.next_node = Node(2)
    head2.next_node.next_node.next_node.next_node.next_node = Node(1)
    print("Is Palindrome: " + str(check_palindrome(head2)))  # True
