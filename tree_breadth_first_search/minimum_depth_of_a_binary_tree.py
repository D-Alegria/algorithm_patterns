"""
    Find the minimum depth of a binary tree.
    The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.
"""

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_minimum_depth(root_node: TreeNode) -> int:  # S = O(N) T = O(N)
    queue = deque()
    queue.append(root_node)
    result = 0

    while queue:
        result += 1
        len_level = len(queue)

        for i in range(len_level):
            current = queue.popleft()

            if current.left is None and current.right is None:
                return result

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)
    return result


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
