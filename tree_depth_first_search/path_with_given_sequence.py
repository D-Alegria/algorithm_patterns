"""
    Given a binary tree and a number sequence,
    find if the sequence is present as a root-to-leaf path in the given tree.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root_node, sequence, index=0):
    if not root_node:
        return False

    if sequence[index] != root_node.val:
        return False

    if not root_node.right and not root_node.left:
        return True

    return find_path(root_node.left, sequence, index + 1) or find_path(root_node.right, sequence, index + 1)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))
