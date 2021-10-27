"""
    Given a binary tree,
    return an array containing nodes in its right view.
    The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.
"""

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_right_view(root_node: TreeNode) -> [TreeNode]:  # S = O(N)  T = O(N)
    sol = []
    queue = deque()

    queue.append(root_node)

    while queue:
        len_level = len(queue)
        for i in range(len_level):
            current = queue.popleft()

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

            if i == len_level - 1:
                sol.append(current)
    return sol


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end='')
    print()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end='')
