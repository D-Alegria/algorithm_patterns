"""
    Given a binary tree,
    connect each node with its level order successor.
    The last node of each level should point to the first node of the next level.
"""

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

    def print_tree(self):
        print("Traversal using 'next' pointer: ", end='')
        current = self
        while current:
            print(str(current.val) + " ", end='')
            current = current.next


def connect_all_siblings(root_node: TreeNode) -> None:  # S = O(N)  T = O(N)
    if root_node is None:
        return

    queue = deque()
    queue.append(root_node)
    currentNode = None

    while queue:
        current = queue.popleft()
        if currentNode:
            currentNode.next = current
        currentNode = current

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_all_siblings(root)
    root.print_tree()
