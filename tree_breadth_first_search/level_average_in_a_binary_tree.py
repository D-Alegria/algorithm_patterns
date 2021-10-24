"""
    Given a binary tree,
    populate an array to represent the averages of all of its levels.
"""

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def traversal(root_node) -> [int]:  # S = O(N) T = O(N)
    result = []

    queue = deque()
    queue.append(root_node)

    while queue:
        level = 0
        len_level = len(queue)

        for i in range(len_level):
            current = queue.popleft()

            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

            level += current.val
        result.append(level / len_level)

    return result


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("level order average traversal: " + str(traversal(root)))
