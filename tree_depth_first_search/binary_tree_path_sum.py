"""
    Given a binary tree and a number ‘S’,
    find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def has_path(root_node, s):
    if not root_node:
        return False

    if root_node.val == s and not root_node.left and not root_node.right:
        return True

    return has_path(root_node.left, s - root_node.val) or has_path(root_node.right, s - root_node.val)


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))
