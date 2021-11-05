"""
    Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number.
    Find the total sum of all the numbers represented by all paths.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_all_numbers(root_node) -> int:
    if not root_node:
        return 0

    return root_node.val + find_sum_of_all_numbers(root_node.left) + find_sum_of_all_numbers(root_node.right)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total sum of Path Numbers: " + str(find_sum_of_all_numbers(root)))
