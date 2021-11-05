"""
    Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number.
    Find the total sum of all the numbers represented by all paths.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_all_paths(root_node, currentSum):
    if not root_node:
        return 0
    currentSum += root_node.val
    if not root_node.left and not root_node.right:
        return currentSum
    return get_all_paths(root_node.left, currentSum * 10) + get_all_paths(root_node.right, currentSum * 10)


def find_sum_of_path_numbers(root_node) -> int:
    return get_all_paths(root_node, 0)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))
