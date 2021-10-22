"""
    Problem Statement

    Given a binary tree,
    populate an array to represent its level-by-level traversal.
    You should populate the values of all nodes of each level from left to right in separate sub-arrays.


"""
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def traversal(root_node):
    result = []
    queue = deque()

    queue.append(root_node)

    while queue:
        level = []
        for x in range(len(queue)):
            temp = queue.popleft()
            level.append(temp.val)
            if temp.left is not None:
                queue.append(temp.left)
            if temp.right is not None:
                queue.append(temp.right)
        result.append(level)
    return result


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traversal(root)))
