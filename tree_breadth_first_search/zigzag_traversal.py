"""
    Given a binary tree,
    populate an array to represent its zigzag level order traversal.
    You should populate the values of all nodes of the first level from left to right,
    then right to left for the next level and keep alternating in the same manner for the following levels.
"""
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def traverse(root_node: TreeNode) -> [[int]]:  # S = O(N) T = O(N)
    queue = deque()
    result = []
    alt = False

    if root_node is None:
        return result

    queue.append(root_node)

    while queue:
        level = deque()
        len_level = len(queue)

        for i in range(len_level):
            current = queue.popleft()
            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)
            if alt:
                level.appendleft(current.val)
            else:
                level.append(current.val)
        alt = not alt
        result.append(list(level))
    return result


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))
