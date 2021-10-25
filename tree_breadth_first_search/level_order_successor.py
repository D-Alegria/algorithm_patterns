"""
    Given a binary tree and a node,
    find the level order successor of the given node in the tree.
    The level order successor is the node that appears right after the given node in the level order traversal.
"""

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_successor(root_node: TreeNode, key: int) -> TreeNode:  # S = O(N)  T = O(N)
    queue = deque()
    queue.append(root_node)

    while queue:
        current = queue.popleft()

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
        if current.val == key:
            return queue.popleft()

    return None


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    result = find_successor(root, 12)
    if result:
        print(result.val)
    result = find_successor(root, 9)
    if result:
        print(result.val)
